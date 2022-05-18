#!/usr/bin/env python3
"""instantiate the Babel object in your app. Store it in a module-level
variable named babel"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """configure available languages in our app and set Babel’s default locale
    "en" and timezone "UTC"."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route('/')
def index():
    """Create a single "/" route and an index.html template that simply
    outputs"""
    return render_template('1-index.html')


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    """ Main Function """
    app.run()
