from pet_posts.handlers import echo, pet, start
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def init(api_token):
    updater = Updater(token=api_token, use_context=True)
    return updater


def configure(dispatcher):
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)
    # Handle all text except /<command> messages
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    pet_handler = CommandHandler("pet", pet)
    dispatcher.add_handler(pet_handler)
    return dispatcher


def run(updater):
    updater.start_polling()
