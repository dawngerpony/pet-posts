Create the project and push to heroku:

```shell

heroku create
git push heroku main

# error message: No default language could be detected for this app.
# presumably because of a lack of requirements.txt


```

Add Poetry buildpack https://elements.heroku.com/buildpacks/moneymeets/python-poetry-buildpack

```shell
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
git push heroku main

# remote: -----> ^3.9 is not valid, please specify an exact Python version (e.g. 3.8.1) in your pyproject.toml (and thus poetry.lock)

```
