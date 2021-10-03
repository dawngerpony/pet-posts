from pet_posts.handlers import echo, pet, start


def test_start(mocker):
    update = mocker.Mock()
    context = mocker.Mock()
    start(update, context)
    context.bot.send_message.assert_called_once()


def test_echo(mocker):
    update = mocker.Mock()
    context = mocker.Mock()
    echo(update, context)
    context.bot.send_message.assert_called_once()


def test_pet(mocker):
    update = mocker.Mock()
    context = mocker.Mock()
    pet(update, context)
    context.bot.send_photo.assert_called_once()
