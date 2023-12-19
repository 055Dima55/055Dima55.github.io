"""
2) Напишіть 5 тестів з затримкою в 2 секунди кожен,
один з тестів повинен мати унікальне імя.
Запустіть їх за домогою pytest-xdist ліби в 5 потоків
Запустіть цей ваш унікальний тест з маркером -k
додайте скірншоти виконання
(не забудьте додавати -v, що б я бачив що ви проганяли)
біля скріншотів пропишіть команди
які ви використовували.
3) обновіть requirements.txt
"""
import time

import pytest


def test_slip():
    time.sleep(2)


def test_wait_1():
    time.sleep(2)


def test_stay_1():
    time.sleep(2)


def test_stay_2():
    time.sleep(2)


def test_wait_2():
    time.sleep(2)
