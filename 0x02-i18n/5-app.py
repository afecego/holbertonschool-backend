#!/usr/bin/env python3
"""Basic Flask app"""
from typing import Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class that has a LANGUAGES class attribute equal to ["en", "fr"] and
    et Babel’s default locale ("en") and timezone ("UTC")."""
    LANGUAGE = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('5-app.Config')


@app.route('/', strict_slashes=False)
def index():
    """Create a single '/' route and an index.html template that simply
    outputs"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages.
    detect if the incoming request contains locale argument and ifs
    value is a supported locale"""
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGE']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGE'])


def get_user() -> Union[dict, None]:
    """returns a user dictionary or None if the ID cannot be found or if
    login_as was not passed"""
    if request.args.get('login_as'):
        a = int(request.args.get('login_as'))
        dicc = users.get(a)
        if dicc:
            return dicc
    return None


@app.before_request
def before_request():
    """should use get_user to find a user if any, and set it as a
    global on flask.g.user"""
    g.user = get_user()


if __name__ == '__main__':
    """Main function"""
    app.run(debug=True)
