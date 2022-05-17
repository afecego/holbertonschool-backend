#!/usr/bin/env python3
"""setup a basic Flask app """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Create a single "/" route and an index.html template that simply
    outputs"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run()
