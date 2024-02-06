#!/usr/bin/env python3

"""
Create a route using flask.
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"])
def render_index():
    """
    Render index.html
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
