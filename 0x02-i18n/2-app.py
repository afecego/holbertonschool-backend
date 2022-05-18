#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """class that has a LANGUAGES class attribute equal to ["en", "fr"] and
    set Babel’s default locale ("en") and timezone ("UTC")."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


configuration = Config()


app = Flask(__name__)
app.config.from_object(configuration)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """Create a single '/' route and an index.html template that simply
    outputs"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """Create a get_locale function with the babel.localeselector and
    determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    """Main function"""
    app.run()

