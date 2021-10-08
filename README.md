# Pet Posts

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Telegram bot to post cute animal pictures.

## To get set up locally

Prerequisite: Python 3.9+, Poetry, a Telegram bot API key

```shell
poetry install
echo "<API_KEY>" > .env
poetry run pytest
```

To run the bot:

```shell
poetry run python app.py
# or
poetry shell
python app.py
```

To run the bot with hot reloading (see [jurigged][jurigged] docs for more info):

```shell
poetry run jurigged app.py
# or
poetry run python -m jurigged app.py
```

To run the tests:

```shell
tox
```

To fix formatting issues:

```shell
tox -e format
```

## Backlog

- Allow the retrieval of a specific animal type e.g. `/pet fox`
- Show all animal types e.g. `/pets`
- Migrate image URLs into a proper database
- Integrate with various Twitter accounts to build up database of animals

## Resources

The following resources were helpful to me when building this bot:

- https://www.process.st/telegram-bot/ (Ruby)
- https://python-telegram-bot.readthedocs.io/en/stable/
- https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
- https://core.telegram.org/bots#6-botfather
- https://github.com/koxudaxi/poetry-pycharm-plugin
- https://pythonawesome.com/hot-reloading-for-python/

[jurigged]: https://pypi.org/project/jurigged/
