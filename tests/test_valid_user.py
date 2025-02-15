"""This module contains test cases for the valid user route."""
# Third party imports
import pytest

# Local application imports
from app.app import app


@pytest.fixture(name="client")
def create_client():
    """Initialize a fixture test client for flask unit testing."""
    with app.test_client() as app_client:
        yield app_client


def test_valid_user_content(client):
    """Flask unit testing for content in valid parameter page."""
    response = client.get("/user/jack")
    assert response.status_code == 200
    assert b"JACK" in response.data
