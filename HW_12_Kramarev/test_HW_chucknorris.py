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


@pytest.mark.usefixtures('fixture_random')
class TestRandom:
    def test_icon_url_not_empty(self, fixture_random):
        assert self.response.json()["icon_url"] is not None

    def test_icon_url_png(self, fixture_random):
        assert self.response.json()["icon_url"].endswith(".png")

    def test_value_not_empty(self, fixture_random):
        assert self.response.json()["value"] is not None

    def test_value_meaning(self, fixture_random):
        assert len(self.response.json()["value"]) > 10


@pytest.mark.usefixtures("chuck_norris_api")
class TestSpecificWord:
    def test_specific_word(self):
        print(self.response.text)

    def test_status_code(self):
        assert self.response.status_code == 200

    def test_number_of_jokes_check_rusult(self):
        assert "result" in self.j_son

    def test_numbers_of_jokes(self):
        numbers_of_jokes = len(self.j_son["result"])
        assert numbers_of_jokes > 0
        print(f"Numbers of jokes {numbers_of_jokes}")

    def test_specific_joke(self):
        specific_of_joke = "Chuck Norris is not hung like a horse. Horses are hung like Chuck Norris."
        jokes = [joke['value'] for joke in self.j_son["result"]]
        assert specific_of_joke in jokes
