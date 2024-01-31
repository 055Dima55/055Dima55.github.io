import pytest
import requests


@pytest.fixture(scope="class")
def fixture_random(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/random")
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
    yield response, status_code


@pytest.fixture(scope="class")
def chuck_norris_api(request):
    URL = "https://api.chucknorris.io/jokes/search?query=Horses"
    response = requests.request(method="GET", url=URL)
    request.cls.response = response
    j_son = response.json()
    request.cls.j_son = j_son
    yield response, j_son
