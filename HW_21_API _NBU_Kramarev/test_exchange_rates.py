from datetime import datetime
import pytest


@pytest.mark.usefixtures('fixture_exchange_rates')
class TestsNBU:

    def test_exchange_rates(self):
        with open("results.txt", "a") as f:
            f.write(f"{datetime.now()} - Дата створення запиту\n")
            for i, currency in enumerate(self.response.json(), 1):
                f.write(f"{i}. {currency['txt']} to UAH: {currency['rate']}\n")



