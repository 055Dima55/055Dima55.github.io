'''
2-ий файл з трьома тестами який буде тестити ці три функції. В кожному тесті 1 тест.
В тестових функціях ми ставимо типізацію. В першому файлі в всіх функціях проставляємо що приймає і що повертає.
 Встановіть собі пайтест і прораньте. До домашки отрім кода додайте скріншот прогона тестів. '''

from HW_file_1 import sorted_list
from HW_file_1 import sorted_list_revers
from HW_file_1 import sorted_list_words

def test_sorted_list():
    assert sorted_list([200, 3, 4, 6, 70, 1, 3, 44]) == [1, 3, 3, 4, 6, 44, 70, 200]

def test_sorted_revers():
    assert sorted_list_revers([200, 300, 45, 60, 70, 1, 3, 44]) == [300, 200, 70, 60, 45, 44, 3, 1]

def test_sorted_words():
    assert  sorted_list_words(['яблука', 'банани', 'ківі', 'кавун', 'хліб']) == ['ківі', 'хліб', 'кавун', 'яблука', 'банани']
