'''перевірити поля "icon_url" чи він не пусти
+ чи це картинка,  - 2 теста
перевірити чи є ключ "value"
і перевірити його значення - 2 теста
Зробити окремий клас
пошук жарту по конретному
слову  https://api.chucknorris.io/jokes/search?query={query}
зробити класому фікстуру
тест на статус код
тест на кількість жартів
тест на сам жарт
+ 3 тести '''

import pytest
import requests


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    def test_icon_url_not_empty(self):
        assert self.response.json()["icon_url"] is not None

    def test_icon_url_png(self):
        assert self.response.json()["icon_url"].endswith(".png")

    def test_value_not_empty(self):
        assert self.response.json()["value"] is not None

    def test_value_meaning(self):
        assert int(self.response.json()["value"]) > 10



@pytest.SpecificWordfixture(scope="class")
def chuck_norris_api():
    URL = "https://api.chucknorris.io/jokes/search?query=Horses"
    response = requests.request(method="GET", url=URL)
    return response


@pytest.SpecificWord("chuck_norris_api")
class TestSpecificWord:
    def test_specific_word(self):
        print(chuck_norris_api.text)

    def test_status_code(self, chuck_norris_api):
        URL = "https://api.chucknorris.io/jokes/search?query=Horses"
        response = requests.request(method="GET", url=URL)
        assert response.status_code == 200

    def test_number_of_jokes(self):
        URL = "https://api.chucknorris.io/jokes/search?query=Horses"
        response = requests.request(method="GET", url=URL)
        j_son = response.json()
        assert "result" in j_son
        nambers_of_jokes = len(j_son["result"])
        assert nambers_of_jokes > 0
        print(f"Numbers of jokes {nambers_of_jokes}")

    def test_specific_joke(self):
        specific_of_joke = "Chuck Norris is not hung like a horse. Horses are hung like Chuck Norris."
        URL = "https://api.chucknorris.io/jokes/search?query=Horses"
        response = requests.request(method="GET", url=URL)
        j_son = response.json()
        assert "result" in j_son
        jokes = [joke['value'] for joke in j_son["result"]]
        assert specific_of_joke in jokes
