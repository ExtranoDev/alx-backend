#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """" set Babel’s default locale and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determine the best match from supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Displays value to html page"""
    return render_template('5-index.html')


@app.before_request
def before_request():
    """"""
    g.user = get_user()

def get_user():
    """"""
    user_id = request.args.get('login_as')
    if user_id in users.keys():
        return users.get(int(user_id))
    return None


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
