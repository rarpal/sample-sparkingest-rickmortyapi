from common.client import get_rest_api
import extract.character
import extract.episode
import extract.location

def test_get_rest_api_character():
    l = get_rest_api("https://rickandmortyapi.com/api/character")

    assert l != None

def test_get_rest_api_episode():
    l = get_rest_api("https://rickandmortyapi.com/api/episode")

    assert l != None

def test_get_rest_api_location():
    l = get_rest_api("https://rickandmortyapi.com/api/location")

    assert l != None

def test_extract_character():
    assert None
    ## TODO
    # assert existence of columns
    # assert existence of rows

def test_extract_episode():
    assert None
    ## TODO
    # assert existence of columns
    # assert existence of rows

def test_extract_location():
    ## TODO
    assert None
    # assert existence of columns
    # assert existence of rows