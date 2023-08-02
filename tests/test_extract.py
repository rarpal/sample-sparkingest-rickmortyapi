from common.client import get_rest_api

def test_get_rest_api():
    l = get_rest_api("https://rickandmortyapi.com/api/character")

    assert l != None

def test_extract_character():
    pass
    # assert existence of columns
    # assert existence of rows

def test_extract_episode():
    pass
    # assert existence of columns
    # assert existence of rows

def test_extract_location():
    pass
    # assert existence of columns
    # assert existence of rows
