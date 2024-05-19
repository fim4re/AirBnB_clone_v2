#!/usr/bin/python3
""" 4. Add fourth view function that displays var only if is integer """

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


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ replace text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(m):
    """ replace int only if given int. """
    m = str(m)
    return '{} is a number'.format(m)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
