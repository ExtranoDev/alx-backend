#!/usr/bin/env python3
"""Basic Flask app"""
import pytz
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
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # locale from user settings
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    # Locale from request header
    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone() -> str:
    """Infers appropriate timezone"""

    # Timezone from URL parameter
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone

        except pytz.exceptions.UnknownTimeZoneError as e:
            return app.config["BABEL_DEFAULT_TIMEZONE"]

    # Timezone from users preference
    if g.user and g.user.get('timezone') in users.values():
        try:
            timezone = g.user.get('timezone')
            return pytz.timezone(timezone)

        except pytz.exceptions.UnknownTimeZoneError as e:
            return app.config["BABEL_DEFAULT_TIMEZONE"]

    # Default Timezone
    return app.config["BABEL_DEFAULT_TIMEZONE"]


def get_user():
    """ function that returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed"""
    user_id = request.args.get('login_as')
    user_det = users.get(int(user_id)) if user_id else None
    return user_det


@app.before_request
def before_request():
    """"use get_user to find a user if any
    and set it as a global on flask.g.user"""
    g.user = get_user()
    now_utc = datetime.utcnow()
    timezone = pytz.timezone(g.user.get('timezone'))
    now_tz = now_utc.astimezone(timezone)
    g.time = now_tz.strftime("%b %d, %Y, %I:%M:%S %p")


@app.route('/', strict_slashes=False)
def index():
    """Displays value to html page"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
