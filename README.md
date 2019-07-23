This repository is the Python Flask microservice providing a recommendation engine for the [FastTracks](https://github.com/alexander-mathieu/fast_tracks) app, returning Spotify songs based on our users best Power Ranked tracks.

__Installation:__
- `git clone git@github.com:BrennanAyers/flask_tracks.git` (for SSH)
- `cd flask_tracks`
- `python -m venv venv` (for virutal environment)
- `pip install requirements.txt`

- You will also need a `.env` file with a `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET`, gained from creating an App with Spotify.

__Endpoints:__
- `/api/v1/recommended?song_ids=COMMA_SEPERATED_LIST_OF_SPOTIFY_SONG_IDS_MAX_5&limit=INTEGER_FROM_ONE_TO_FIFTY`

__Tests:__
- run `pytest`

__Hosted Version:__
- [Heroku](https://fast-tracks-flask.herokuapp.com)

__Contributors:__
- Brennan Ayers
- Alexander Mathieu
