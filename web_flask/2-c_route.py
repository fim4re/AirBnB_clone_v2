#!/usr/bin/python3
""" 2. Script to start a Flask web application with 3 view functions """

from flask import Flask
# create flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Returns text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ Return more text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ replace it with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
