import os
import requests
import settings

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

def get_token():
    params = { 'grant_type': 'client_credentials' }
    r = requests.post('https://accounts.spotify.com/api/token', auth = (SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET), data = params)
    json = r.json()
    token = json['access_token']
    return token
