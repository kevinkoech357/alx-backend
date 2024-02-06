#!/usr/bin/env python3

"""
Create a route using flask.
Import and configure flask babel.
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel()


class Config:
    """
    Babel configurations
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """
    Get best match for user locale.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/", methods=["GET"])
def render_index():
    """
    Render index.html
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
