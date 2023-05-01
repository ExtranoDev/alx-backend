#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """" set Babel’s default locale and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """determine the best match from supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ function that returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed"""
    user_id = request.args.get('login_as')
    if user_id in users.keys():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """"use get_user to find a user if any
    and set it as a global on flask.g.user"""
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index():
    """Displays value to html page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
