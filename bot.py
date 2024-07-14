# bot.py

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6513332762:AAG87rvx0cFYFfi1q7KmCfMxS1XCvyxQVL0'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Function to handle the /start command
def handle_start(update, context):
    # Send a welcome message
    update.message.reply_text('Welcome to the bot!')

# Function to handle incoming messages
def handle_message(update, context):
    # Echo the received message
    update.message.reply_text(update.message.text)

def main():
    # Create an instance of the bot updater
    updater = Updater(token=bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    start_handler = CommandHandler('start', handle_start)
    dispatcher.add_handler(start_handler)

    # Register the message handler
    message_handler = MessageHandler(Filters.text, handle_message)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()