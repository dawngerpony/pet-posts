from pet_posts import bot


def test_init(mocker):
    mocker.patch("pet_posts.bot.Updater")
    bot.init("test_token")
    bot.Updater.assert_called_once()


def test_configure(mocker):
    updater = mocker.patch("pet_posts.bot.Updater")
    command_handler = mocker.patch("pet_posts.bot.CommandHandler")
    message_handler = mocker.patch("pet_posts.bot.MessageHandler")
    start = mocker.patch("pet_posts.bot.start")
    pet = mocker.patch("pet_posts.bot.pet")
    dispatcher = bot.configure(updater.dispatcher)
    dispatcher.add_handler.assert_called()
    assert 3 == dispatcher.add_handler.call_count
    assert 2 == command_handler.call_count
    assert 1 == message_handler.call_count
    command_handler.assert_any_call("start", start)
    command_handler.assert_any_call("pet", pet)
    message_handler.assert_called()


def test_run(mocker):
    updater = mocker.patch("pet_posts.bot.Updater")
    bot.run(updater)
    updater.start_polling.assert_called_once()
