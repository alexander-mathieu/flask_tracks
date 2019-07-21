import pytest
import vcr
import requests
import spotify_service

@vcr.use_cassette('fixtures/vcr_cassettes/spotify_token.yaml')
def test_get_token():
    r = spotify_service.get_token()
    assert r == 'BQD_E_ZUc6MhGqEz9yf3eYtXtiihmliRoo47OdtELVa5X2IVr1iI_0dovkKuxv22PcoXryPtngccmpE3-UQ'
