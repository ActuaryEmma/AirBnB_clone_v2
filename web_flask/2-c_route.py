#!/usr/bin/python3
""" starts a Flask web app with route /, /hbnb, /c/<text> """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def capture_text(text):
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run()
