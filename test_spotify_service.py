import pytest
import vcr
import spotify_service

@vcr.use_cassette('fixtures/vcr_cassettes/spotify_token.yaml')
def test_get_token():
    r = spotify_service.get_token()
    assert r == 'BQD_E_ZUc6MhGqEz9yf3eYtXtiihmliRoo47OdtELVa5X2IVr1iI_0dovkKuxv22PcoXryPtngccmpE3-UQ'

@vcr.use_cassette('fixtures/vcr_cassettes/spotify_recommended_songs.yaml', record_mode='twice')
def test_get_recommended_songs():
    r = spotify_service.get_recommended_songs('50FHmxsLg0xFT53D9DoZLm,7v7VdqWOygnY3jaIsoUeCs,1269OELfNNvdgMIobuYBBt,7q4N0abbhFfLBXJpyO7EzN,0FgebSbDmDdXpot4VmsgA6', 5)
    for song in r:
        assert 'spotify_id' in song.keys()
        assert 'title' in song.keys()
        assert 'artist' in song.keys()
        assert 'album' in song.keys()
        assert 'spotify_url' in song.keys()
        assert 'album_art_url' in song.keys()
        assert 'length' in song.keys()
