#!/usr/bin/env python3
from dotenv import load_dotenv
from pet_posts.handlers import echo, pet, start
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
    # Handle all text except /<command> messages
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    pet_handler = CommandHandler("pet", pet)
    dispatcher.add_handler(pet_handler)
    updater.start_polling()


if __name__ == "__main__":
    main()
