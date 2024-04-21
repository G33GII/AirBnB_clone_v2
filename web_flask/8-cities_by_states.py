#!/usr/bin/python3
"""
Main module for Flask web application.
"""

# Importing necessary modules and classes
from flask import Flask, render_template
from models import *
from models import storage

# Creating a Flask application instance
app = Flask(__name__)

# Route to display the states and cities listed in alphabetical order


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Route handler to display the states and
    cities listed in alphabetical order."""
    # Retrieve all State objects from the storage
    states = storage.all("State").values()
    # Render the HTML template '8-cities_by_states.html' with the states data
    return render_template('8-cities_by_states.html', states=states)

# Function to close the storage when the application context is torn down


@app.teardown_appcontext
def teardown_db(exception):
    """Function to close the storage when
    the application context is torn down."""
    storage.close()


# Main block to run the Flask application
if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0 at port 5000 in debug mode
    app.run(host='0.0.0.0', port='5000', debug=True)
