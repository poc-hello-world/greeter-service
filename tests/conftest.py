"""Test configuration."""
import pytest

import app as myapp


@pytest.fixture
def app():
    """pytest-flask required function to create multiple instances of our app.

    Returns:
        An application insatnce to be tested.

    """
    return myapp.app
