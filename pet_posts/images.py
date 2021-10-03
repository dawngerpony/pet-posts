import random


def get_image_url():
    with open("image_urls.txt") as f:
        image_urls = f.readlines()
    return random.choice(image_urls)
