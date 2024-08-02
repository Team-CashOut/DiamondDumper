from PyQt5.QtWidgets import QMainWindow

def save_chats_text_history():
    for m_chat_id, messages_dict in messages_by_chat.items():
        print(f"Saving history of {m_chat_id} as a text...")
        new_messages = messages_dict['buf']
        save_text_history(m_chat_id, new_messages)
        messages_by_chat[m_chat_id]['history'] += new_messages
        messages_by_chat[m_chat_id]['buf'] = []


def get_chat_id(message, bot_id):
    m = message
    m_chat_id = 0
    if isinstance(m.peer_id, PeerUser):
        if not m.to_id or not m.from_id:
            m_chat_id = str(m.peer_id.user_id)
        else:
            if m.from_id and int(m.from_id.user_id) == int(bot_id):
                m_chat_id = str(m.to_id.user_id)
            else:
                m_chat_id = str(m.from_id)
    elif isinstance(m.peer_id, PeerChat):
        m_chat_id = str(m.peer_id.chat_id)

    return m_chat_id


def get_from_id(message, bot_id):
    m = message
    from_id = 0
    if isinstance(m.peer_id, PeerUser):
        if not m.from_id:
            from_id = str(m.peer_id.user_id)
        else:
            from_id = str(m.from_id.user_id)
    elif isinstance(m.peer_id, PeerChat):
        from_id = str(m.from_id.user_id)

    return from_id


async def process_message(bot, m, empty_message_counter=0):
    m_chat_id = get_chat_id(m, bot.id)
    m_from_id = get_from_id(m, bot.id)

    is_from_user = m_chat_id == m_from_id

    if isinstance(m, MessageEmpty):
        empty_message_counter += 1
        return True
    elif empty_message_counter:
        print(f'Empty messages x{empty_message_counter}')
        empty_message_counter = 0

    history_tail = False
    message_text = ''

    if m.media:
        if isinstance(m.media, MessageMediaGeo):
            message_text = f'Geoposition: {m.media.geo.long}, {m.media.geo.lat}'
        elif isinstance(m.media, MessageMediaPhoto):
            await save_media_photo(bot, m_chat_id, m.media.photo)
            message_text = f'Photo: media/{m.media.photo.id}.jpg'
        elif isinstance(m.media, MessageMediaContact):
            message_text = f'Vcard: phone {m.media.phone_number}, {m.media.first_name} {m.media.last_name}, rawdata {m.media.vcard}'
        elif isinstance(m.media, MessageMediaDocument):
            full_filename = await save_media_document(bot, m_chat_id, m.media.document)
            filename = os.path.split(full_filename)[-1]
            message_text = f'Document: media/{filename}'
        else:
            print(m.media)
        #TODO: add other media description
    else:
        if isinstance(m.action, MessageActionChatEditPhoto):
            await save_media_photo(bot, m_chat_id, m.action.photo)
            message_text = f'Photo of chat was changed: media/{m.action.photo.id}.jpg'
        elif m.action:
            message_text = str(m.action)
    if isinstance(m, MessageService):
        #TODO: add text
        pass

    if m.message:
        message_text  = '\n'.join([message_text, m.message]).strip()

    text = f'[{m.id}][{m_from_id}][{m.date}] {message_text}'
    print(text)

    if not m_chat_id in messages_by_chat:
        messages_by_chat[m_chat_id] = {'buf': [], 'history': []}

    messages_by_chat[m_chat_id]['buf'].append(text)

    if is_from_user and m_from_id and m_from_id not in all_users:
        full_user = await bot(GetFullUserRequest(int(m_from_id)))
        user = full_user.user
        print_user_info(user)
        save_user_info(user)
        remove_old_text_history(m_from_id)
        await save_user_photos(bot, user)
        all_users[m_from_id] = user

    return False


async def get_chat_history(bot, from_id=0, to_id=0, chat_id=None, lookahead=0):
    print(f'Dumping history from {from_id} to {to_id}...')
    messages = await bot(GetMessagesRequest(range(to_id, from_id)))
    empty_message_counter = 0
    history_tail = True
    for m in messages.messages:
        is_empty = await process_message(bot, m, empty_message_counter)
        if is_empty:
            empty_message_counter += 1

    if empty_message_counter:
        print(f'Empty messages x{empty_message_counter}')
        history_tail = True

    save_chats_text_history()
    if not history_tail:
        return await get_chat_history(bot, from_id+HISTORY_DUMP_STEP, to_id+HISTORY_DUMP_STEP, chat_id, lookahead)
    else:
        if lookahead:
            return await get_chat_history(bot, from_id+HISTORY_DUMP_STEP, to_id+HISTORY_DUMP_STEP, chat_id, lookahead-1)
        else:
            print('History was fully dumped.')
            return None


async def bot_auth(bot_token, proxy=None):
    # TODO: make not global
    global base_path
    bot_id = bot_token.split(':')[0]
    base_path = bot_id
    if os.path.exists(base_path):
        import time
        new_path = f'{base_path}_{str(int(time.time()))}'
        os.rename(base_path, new_path)
        os.mkdir(base_path)
        shutil.copyfile(f'{new_path}/{base_path}.session', f'{base_path}/{base_path}.session')
    else:
        os.mkdir(base_path)

    try:
        bot = await TelegramClient(os.path.join(base_path, bot_id), API_ID, API_HASH, proxy=proxy).start(bot_token=bot_token)
        bot.id = bot_id
    except AccessTokenExpiredError as e:
        print("Token has expired!")
        sys.exit()

    me = await bot.get_me()
    print_bot_info(me)
    user = await bot(GetFullUserRequest(me))
    all_users[me.id] = user

    user_info = user.user.to_dict()
    user_info['token'] = bot_token

    with open(os.path.join(bot_id, 'bot.json'), 'w') as bot_info_file:
        json.dump(user_info, bot_info_file)

    return bot


class DiamondDumperApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        uic.loadUi('dumper', self)

        self.dumpMessage_button.clicked.connect(self.dumpMessages)
        # Connect other button signals as required

        # Set up the console_text_edit widget
        self.console_text_edit.setReadOnly(True)

        # Display initial responses upon launching the script
        self.print_console_message("Reading database...")
        self.print_console_message("Importing information...")
        # Add more initial responses as desired

    def print_console_message(self, message):
        self.console_text_edit.append(message)

    def dumpMessages(self):
        bot_token = self.token_line_edit.text()
        bot = bot_auth(bot_token)
        get_chat_history(bot)

    def print_console_message(self, message):
        self.ui.console_text_edit.append(message)
    
    def start_button_clicked(self):
        pass
    
    def stop_button_clicked(self):
        pass
    
    def setWebhook_button_clicked(self):
        pass
    
    def sendDocument_button_clicked(self):
        pass
    
    def getME_button_clicked(self):
        pass
    
    def sendPhoto_button_clicked(self):
        pass
    
    def sendMessage_button_clicked(self):
        pass
    
    def set_privacy_button_clicked(self):
        pass
    
    def pushButton_7_clicked(self):
        pass
    
    def pushButton_8_clicked(self):
        pass