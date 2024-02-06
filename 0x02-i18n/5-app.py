#!/usr/bin/env python3

"""
Create a route using flask.
Import and configure flask babel.
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


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

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    Get user based on id.
    """
    user = request.args.get("login_as")

    if user:
        try:
            return users.get(int(user))
        except Exception:
            return None
    return None


@app.before_request
def before_request():
    """
    Add user to global scope.
    """
    g.user = get_user()


@app.route("/", methods=["GET"])
def render_index():
    """
    Render index.html
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
