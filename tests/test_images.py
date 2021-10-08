from unittest.mock import patch
from pet_posts.images import get_image_url


def test_get_image_url(mocker):
    url = "https://www.example.com/image.jpg"
    mock_open = mocker.mock_open(read_data=url)
    with patch("pet_posts.images.open", mock_open):
        image_url = get_image_url()
    assert image_url == url
