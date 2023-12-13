'''
1) додайте requirements.txt на ваш гіт
2) Виберіть будь-яку помилку яка вам подобається і зробіть функцію яка перевіряє на цю помилку(в функції try except)
3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма трьома методами
4) перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює
'''


# 2 Виберіть будь-яку помилку яка вам подобається і зробіть функцію яка перевіряє на цю помилку(в функції try except)
#
#def mistake_Type_Error(number1: int, naumber2: int):
#    try:
#        result = number1 + naumber2
#        return result
#    except TypeError as e:
#        print(F"Error: {e}")
#        print("Помилка при складанні числа та рядка.")
#        return None
#
#
#result = mistake_Type_Error(5, "5")
#if result is not None:
#    print(result)

#3) зробіть функцію як ми робили з додаванням тільки
#замість двох чисел зробіть три числа і протестуйте її всіма трьома методами

def add_three_numbers(number_1: int, number_2: int, number_3: int):
    result = number_1 + number_2 + number_3
    return result

'''
4) перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює
from datetime import datetime
import time

def funk_wrapper_time(funс):
    def wrapper(*arg, **kwarg):
        start = datetime.now()
        result = funс(*arg, **kwarg)
        delta_time = datetime.now() - start
        print("Час виконнаня функції сь такий: ", delta_time)
        return result

    return wrapper()


@funk_wrapper_time
def foo_1(*arg, **kwarg):
    print("foo_1")
    time.sleep(1)


@funk_wrapper_time
def foo_2(*arg, **kwarg):
    print("foo_2")
    time.sleep(2)


foo_1()
foo_2()

# чомусь у мене видае помилку TypeError: 'NoneType' object is not callable коли запускаю, але все виконується '''
