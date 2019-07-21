import os
from flask import Flask, request, json, jsonify
import requests
# import config
import base64
# import settings

api = Flask(__name__)

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

@api.route('/', methods = ['GET'])
def home():
    return '<h1>Welcome to the FastTracks Microservice!</h1>'

@api.route('/api/v1/recommendations', methods = ['GET'])
def parse_response():
    ids = request.args.get('song_ids')
    limit = request.args.get('limit')
    return get_recommended_songs(ids, limit)

if __name__ == '__main__':
    api.run()
