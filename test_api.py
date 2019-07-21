import os
import pytest
from api import api

@pytest.fixture()
def client():
    api.config['TESTING'] = True

    with api.test_client() as client:
        yield client

def test_home_page(client):
    r = client.get('/')
    assert b'Welcome to the FastTracks Microservice!' in r.data

def test_get_recommended_songs(client):
    params = {'song_ids': 'stuff', 'limit': 5}

    r = client.get('/api/v1/recommendations?song_ids=stuff&limit=5')
    assert b"{ 'spotify_id': 'spotify_id_1', 'title': 'Song 1', 'artist': 'Artist 1', 'album': 'Album 1', 'spotify_url': 'https://spotify.com/1', 'album_art_url': 'https://art.album.com/1', 'length': 11111 }" in r.data
