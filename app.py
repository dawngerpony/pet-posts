from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import os


def main():
    load_dotenv()  # take environment variables from .env.
    api_token = os.getenv("API_TOKEN")

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    updater = Updater(token=api_token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()


def start(update, context):
    """Respond to '/start' command."""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a banana, please talk to me!"
    )


def echo(update, context):
    """Echo back the contents of a message."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


if __name__ == "__main__":
    main()
