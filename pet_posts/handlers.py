"""Bot handler functions."""
import random


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
    urls = [
        "https://www.southamerica.travel/wp-content/uploads/2018/02/10-amazing-facts-about-Capybara-1.jpg",
        "https://www.zastavki.com/pictures/originals/2015/Animals___Rodents_____Hamster_on_a_rope_092822_.jpg",
        "https://s-i.huffpost.com/gen/2034584/images/o-PUDDING-THE-FOX-facebook.jpg",
        "https://www.zooeasy.com/wp-content/uploads/2019/07/jack-catalano-q1pw1dOW0_0-unsplash.jpg",
        "https://i.huffpost.com/gen/911965/images/o-CUTEST-BABY-ANIMAL-facebook.jpg",
    ]
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=random.choice(urls))
