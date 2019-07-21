from flask import Flask, request, json, jsonify
import requests
# import config
import base64
# import settings

api = Flask(__name__)

@api.route('/', methods = ['GET'])
def home():
    return '<h1>Welcome to the FastTracks Microservice!</h1>'
