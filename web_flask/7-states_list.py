#!/usr/bin/python3
"""
Main module for Flask web application.
"""


# Importing necessary modules and classes
from models import *
from models import storage
from flask import Flask, render_template

# Creating a Flask application instance
app = Flask(__name__)

# Route to display the list of states


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Route handler to display the list of states."""
    # Retrieve all State objects from the storage and sort them by name
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    # Render the HTML template '7-states_list.html' with the states data
    return render_template('7-states_list.html', states=states)


# Function to close the storage when the application context is torn down


@app.teardown_appcontext
def teardown_db(exception):
    """Function to close the storage
    when the application context is torn down."""
    storage.close()


# Main block to run the Flask application
if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0 at port 5000 in debug mode
    app.run(host='0.0.0.0', port='5000', debug=True)
