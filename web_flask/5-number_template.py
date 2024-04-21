#!/usr/bin/python3
"""Flask Script"""


from flask import Flask, render_template

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

# Define a route that displays "Python " followed by the value of the text variable


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)  # Default value is "is cool"
def python(text='is_cool'):
    # Replace underscore symbols (_) with a space
    text = text.replace('_', ' ')
    return 'Python ' + text

# Define a route that displays "n is a number" only if n is an integer


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'

# Define a route that displays an HTML page with the number n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    # Render the HTML template with the value of n
    return render_template('5-number.html', number=n)


# Run the Flask application on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
