from common.client import get_rest_api

def test_get_rest_api():
    l = get_rest_api("https://rickandmortyapi.com/api/character")

    assert l != None