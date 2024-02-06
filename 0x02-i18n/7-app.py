#!/usr/bin/env python3

"""
Create a route using flask.
Import and configure flask babel.
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Babel configurations
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Get best match for user locale.
    """
    # Check if the 'locale' parameter is present in the request URL
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    # Check if a user is logged in and has a preferred locale set
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user.get("locale")

    # Use the request header to determine the best match for locale
    best_match = request.accept_languages.best_match(app.config["LANGUAGES"])
    if best_match:
        return best_match

    # If no supported locale is found, fallback to the default locale
    return app.config["BABEL_DEFAULT_LOCALE"]


@babel.timezoneselector
def get_timezone():
    """
    Use users defined timezone if available.
    """
    # Check if the 'timezone' parameter is present in the request URL
    timezone = request.args.get("timezone")
    if timezone:
        try:
            pytz.timezone(timezone)  # Validate if it's a valid time zone
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Check if a user is logged in and has a preferred time zone set
    if g.user and g.user.get("timezone"):
        try:
            pytz.timezone(g.user.get("timezone"))
            return g.user.get("timezone")
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return "UTC"


def get_user(user_id):
    """
    Get user based on id.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Add user to global scope.
    """
    user_id = request.args.get("login_as")
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@app.route("/", methods=["GET"])
def render_index():
    """
    Render index.html
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
