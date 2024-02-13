import pytest
import requests


@pytest.fixture(scope="class")
def fixture_exchange_rates(request):
    URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.request(method="GET", url=URL)
    request.cls.response = response
    yield response
