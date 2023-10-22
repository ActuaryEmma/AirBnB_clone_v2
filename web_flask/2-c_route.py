#!/usr/bin/python3
""" starts a Flask web app with route /, /hbnb, /c/<text> """

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def capture_text(text):
    return f"C {text}"


if __name__ == '__main__':
    app.run()
