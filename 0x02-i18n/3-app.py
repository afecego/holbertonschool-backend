#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class that has a LANGUAGES class attribute equal to ["en", "fr"] and
    et Babel’s default locale ("en") and timezone ("UTC")."""
    LANGUAGE = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('3-app.Config')


@app.route('/', strict_slashes=False)
def index():
    """Create a single '/' route and an index.html template that simply
    outputs"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGE'])


if __name__ == '__main__':
    """Main function"""
    app.run()
