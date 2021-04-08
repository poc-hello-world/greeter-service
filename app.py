"""Example greeting micro-service.

This module implements a greeting service to be used for demos.

Example:
    For a "Hello World", this application would return "Hello".

    Other options would include "Hey" or "Bonjour".
"""
import json

from flask import Flask
from flask_cors import CORS

HTTP_OK = 200
APP_VERSION = 'dev'

app = Flask(__name__)
cors = CORS(app)


@app.route('/status/alive', methods=['GET'])
def alive():
    """Status check function to verify the server can start.

    Returns:
        JSON-formated response.
    """
    response = {
        'status': 'Greeter service is alive',
    }

    return app.response_class(
        response=json.dumps(response),
        status=HTTP_OK,
        mimetype='application/json',
    )


@app.route('/status/healthy', methods=['GET'])
def healthy():
    """Status check function to verify the server can serve requests.

    Returns:
        JSON-formated response.
    """
    response = {
        'status': 'Greeter service is healthy',
    }

    return app.response_class(
        response=json.dumps(response),
        status=HTTP_OK,
        mimetype='application/json',
    )


@app.route('/', methods=['GET'])
def index():
    """Return a greeting.

    Returns:
        JSON-formated response.
    """
    greeting = {
        'greeting': 'hello',
    }

    return app.response_class(
        response=json.dumps(greeting),
        status=HTTP_OK,
        mimetype='application/json',
    )


@app.after_request
def after_request_func(response):
    """Add helpful headers to the response.

    Args:
        response: the Flask-provided response object.

    Returns:
        Proper response, with added headers.
    """
    response.headers['X-Reply-Service'] = 'greeter-service'
    response.headers['X-Version'] = APP_VERSION
    return response
