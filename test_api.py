import os
import pytest
from api import api
import vcr
import json

@pytest.fixture()
def client():
    api.config["TESTING"] = True

    with api.test_client() as client:
        yield client

def test_home_page(client):
    r = client.get('/')
    assert b'Welcome to the FastTracks Microservice!' in r.data

@vcr.use_cassette('fixtures/vcr_cassettes/api_recommended_songs.yaml', decode_compressed_response=True)
def test_get_recommended_songs(client):

    r = client.get('/api/v1/recommendations?song_ids=2MIcpZ7MBeCUEVFDBqU7Ei,4v6dF5830rtgjYr0uov248,2SpLqYLZ5GQTFTDwA4xwGS&limit=5')

    assert [{'album': '魂 Map the Soul', 'album_art_url': 'https://i.scdn.co/image/88c820afe7a607e8de4043d8dd130f2bb70fa769', 'artist': 'Epik High', 'length': 273146, 'spotify_id': '5D1vzchjH805WYLLVpeUjr', 'spotify_url': 'https://open.spotify.com/track/5D1vzchjH805WYLLVpeUjr', 'title': 'Map the Soul (Worldwide Version) [feat. Tablo, MYK & Kero One]'}] == json.loads(r.data)
