"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import render_template
from flask import Flask
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.route('/calculator')
def calculator(name = None):
  """Return me templates at application /me URL."""
  return render_template('calculator.html',name=name)