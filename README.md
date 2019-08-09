# FlaskTracks

## About

Welcome to _FlaskTracks_! FlaskTracks is a micro-service providing a recommendation engine for [FastTracks](https://github.com/alexander-mathieu/fast_tracks/), returning Spotify songs based a user's top songs by power ranking. FlaskTracks was created by [Brennan Ayers](https://github.com/BrennanAyers/) and [Alexander Mathieu](https://github.com/alexander-mathieu/) during Module 3 at [Turing School of Software & Design](https://turing.io/).

The deployed site can be visited [here](https://fast-tracks-flask.herokuapp.com/).

## Installation

```
$ git clone git@github.com:alexander-mathieu/flask_tracks.git
$ cd flask_tracks
$ python -m venv venv (to setup virtual environment)
$ pip install -r requirements.txt
```

You will also need to create a `.env` file with a `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` defined. Both can be gained by creating an application with [Spotify](https://developer.spotify.com/dashboard/).

## API Exploration

Once installation is complete, explore the various API endpoints with the following steps:
* From the `flask_tracks` project directory, boot up a server with `python api.py`
* Open your browser, and visit `http://localhost:3000/`
* Append the following URI to `http://localhost:3000/` in your browser:
```
api/v1/recommended?song_ids=UP_TO_5_COMMA_SEPARATED_SPOTIFY_SONG_IDS&limit=INTEGER_FROM_ONE_TO_FIFTY
```

## Running Tests

Tests can be run with `pytest`.

Example of expected output:
```
============================================================================== test session starts ===============================================================================
platform darwin -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: /Users/alexandermathieu/turing/mod_3/projects/flask_tracks
plugins: vcr-1.0.2, requests-mock-1.6.0
collected 2 items

test_spotify_service.py ..                                                                                                                                                 [100%]
```
