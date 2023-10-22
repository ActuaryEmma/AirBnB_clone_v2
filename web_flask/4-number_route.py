#!/usr/bin/python3
""" script that starts a Flask web app /, /hbnb, /c/<text>, /python/<text> """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def dis_text(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def num_n(n):
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run()
