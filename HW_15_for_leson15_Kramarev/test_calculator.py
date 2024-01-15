'''3) Напишіть тестовий клас який буде тестити
 попередній калькулятор тільки додавання і ділення.
 до кожної математичної дії зробіть 5 тестів
 (використовуйте параметрайз,не пишіть руками зайвого).
 Зробіть класову фікстуру(класметод)
 для сетапа і тердауна сетпа буде писати повідомлення в файл
  коли ми запустили тест
 та текстове повідомлення що ми стартанули.
 Тердаун буде писати повідомлення що ми закінчили і також час коли закінчили
 використайте вже відому вам бібліотеку дататайм
'''

from HW import calk
import pytest
import datetime


class Tests:

    @pytest.mark.parametrize("x, y, result", [
        pytest.param(5, 2, 7, id="first"),
        pytest.param(0, 2, 2, id="second"),
        pytest.param(-1, 2, 1, id="third"),
        pytest.param(-1, -2, -3, id="fourth"),
        pytest.param(100, -100, 0, id="fifth")])
    def test_addition(self, x, y, result):
        current_time = datetime.datetime.now()
        print(f"Running test at: {current_time}")
        assert calk.addition(x, y) == result

    @pytest.mark.parametrize("x, y, result", [
        pytest.param(10, 2, 5, id="first"),
        pytest.param(2, 2, 1, id="second"),
        pytest.param(-5, 2, -2.5, id="third"),
        pytest.param(-20, -10, 2, id="fourth"),
        pytest.param(100, 0, "Не ділимо на 0", id="fifth")])
    def test_division(self, x, y, result):
        current_time = datetime.datetime.now()
        print(f"Running test at: {current_time}")
        assert calk.division(x, y) == result
