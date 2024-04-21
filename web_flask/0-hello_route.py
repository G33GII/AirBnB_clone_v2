#!/usr/bin/python3
"""Flask script"""


from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route that displays "Hello HBNB!"


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


# Run the Flask application on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
