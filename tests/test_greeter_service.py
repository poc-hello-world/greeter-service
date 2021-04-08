# flake8: noqa
"""Application tests."""
from flask import url_for

HTTP_OK = 200


def test_alive_response(client):
    """Test aliveness endpoint.

    Args:
        client: a pytesy-flask-provided application instance.

    """
    res = client.get(url_for('alive'))
    assert res.headers['Content-Type'] == 'application/json'
    assert res.headers['X-Reply-Service'] == 'greeter-service'
    assert res.status_code == HTTP_OK
    assert res.data == b'{"status": "Greeter service is alive"}'


def test_readiness_response(client):
    """Test readiness endpoint.

    Args:
        client: a pytesy-flask-provided application instance.

    """
    res = client.get(url_for('healthy'))
    assert res.headers['Content-Type'] == 'application/json'
    assert res.headers['X-Reply-Service'] == 'greeter-service'
    assert res.status_code == HTTP_OK
    assert res.data == b'{"status": "Greeter service is healthy"}'


def test_index_response(client):
    """Test homepage.

    Args:
        client: a pytesy-flask-provided application instance.

    """
    res = client.get(url_for('index'))
    assert res.headers['Content-Type'] == 'application/json'
    assert res.headers['X-Reply-Service'] == 'greeter-service'
    assert res.status_code == HTTP_OK
    assert res.data == b'{"greeting": "hello"}'
