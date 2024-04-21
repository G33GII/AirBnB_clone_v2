#!/usr/bin/python3
"""Flask Script"""


from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route that displays "Hello HBNB!"


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

# Define a route that displays "HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

# Define a route that displays "C " followed by the value of the text variable


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    # Replace underscore symbols (_) with a space
    text = text.replace('_', ' ')
    return 'C ' + text


# Run the Flask application on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
