#!/usr/bin/env python3
from dotenv import load_dotenv
from pet_posts import bot

import logging
import os


def main():
    load_dotenv()  # take environment variables from .env.
    api_token = os.getenv("API_TOKEN")

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    updater = bot.init(api_token)
    bot.configure(updater.dispatcher)
    bot.run(updater)


if __name__ == "__main__":
    main()
