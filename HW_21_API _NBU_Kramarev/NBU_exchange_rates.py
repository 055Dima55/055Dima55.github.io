from datetime import datetime

import requests


def test_exchange_rates():
    URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(URL)
    exchange_rates = response.json()

    rates = [f"{datetime.now()} - Дата створення запиту\n"]
    for i, currency in enumerate(exchange_rates, 1):
        rates.append(f"{i}. {currency['txt']} to UAH: {currency['rate']}\n")

    with open("results.txt", "a") as f:
        f.writelines(rates)
