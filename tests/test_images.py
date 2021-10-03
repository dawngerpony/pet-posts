from pet_posts.images import get_image_url


def test_get_image_url():
    image_url = get_image_url()
    assert image_url.startswith("http")
