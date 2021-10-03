"""Bot handler functions."""
from pet_posts.images import get_image_url


def start(update, context):
    """Respond to '/start' command."""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a banana, please talk to me!"
    )


def echo(update, context):
    """Echo back the contents of a message."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def pet(update, context):
    """Send a cute picture."""
    image_url = get_image_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)
