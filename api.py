from flask import Flask, request, json, jsonify
import requests
import base64
import spotify_service

api = Flask(__name__)

@api.route('/', methods = ['GET'])
def home():
    return '<h1>Welcome to the FastTracks Microservice!</h1>'

@api.route('/api/v1/recommended', methods = ['GET'])
def parse_request():
    ids = request.args.get('song_ids')
    limit = request.args.get('limit')
    return jsonify(spotify_service.get_recommended_songs(ids, limit))

if __name__ == '__main__':
    api.run()
