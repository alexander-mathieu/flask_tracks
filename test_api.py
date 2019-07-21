import os
import pytest
from api import api

@pytest.fixture
def client():
    api.config['TESTING'] = True

    with api.test_client() as client:
        yield client

def test_home_page(client):
    r = client.get('/')
    assert b'Welcome to the FastTracks Microservice!' in r.data
