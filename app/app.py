"""This module contains the Flask application for CPS3500."""
# Third party imports
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """Default route to display Hello CPS3500!"""
    return "Hello CPS3500!"


@app.route('/new_page')
def new_page():
    """Route to display This is a New Page!"""
    return "This is a New Page!"


@app.route('/user/<username>')
def user_page(username):
    """Route to display personalized message based on username."""
    return render_template('user.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)