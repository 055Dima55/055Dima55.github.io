'''Візьміть дві задачі з попередніх уроків,
перша легка по вирішенню(декілька стрічок),
друга більш складна і перепишіть їх на функції.
Памятайте про Атамарність та god object.
Там де написано що користувач має щось ввести то перероблюємо на функція приймає.
Подивіться може можна за допомогою функції спростити код.
В домашку вставте будь ласка опис задачі (далі(один з наступних уроків) буде домашка вашу домашку покрити тестами,
але ми трохи поміняємо варіанти). '''

''' 1 Школярі та яблука
 n школярів ділять k яблук порівну, недільний залишок залишається в кошику.
 Скільки яблук дістанеться кожному школярові та скільки залишиться в кошику?
 Програма отримує на вхід числа n і k - цілі, додатні, не перевищують 10000.

numN = int(input("Кількість школярів "))
numK = int(input("Кількість яблук "))
num = numK // numN
num2 = numK % numN

print("Школяри отрумають по", num, "залишається в кошику", num2) 
'''
#
# def counting_apples(apple: int, student: int):
#    student_receive = apple // student
#    basket = apple % student
#    printing_result = f"Школяри отрумають по {student_receive}, залишається в кошику {basket}"
#    return printing_result
#
#
# поки зробив так, но я так розумію що в ідеалі ії треба розділити на дві функції, чи так гуд
# result_1 = counting_apples(student=10, apple=13)
# print(result_1)
#
'''Задача 2
Напишіть програму яка в користувача запитує два числа(можуть бути числа типу інт, а можуть бути в стр).
Потім запитує це стр чи інт і в залежності від відповіді конкатенує їх або додає і повертає результат перемножений на три.
якщо після конкатенації отримали 10 то перемноживши на 3 отримаємо 30. 

var_1 = input("Введіть число ")
var_2 = input("Введіть число ")

variant = input("Введіть 'int' або 'str' ")

if variant == "int":
   print((int(var_1) * int(var_2)) * 3)
elif variant == "str":
   print((var_1 + var_2) * 3)

'''
def variant_int(var_int_1: int, var_int_2: int):
    if isinstance(var_int_1, int) and isinstance(var_int_2, int):
        return var_int_1 * var_int_2 * 3


def variant_str(var_str_1: str, var_str_2: str):
    if isinstance(var_str_1, str) and isinstance(var_str_2, str):
        return (var_str_1 + var_str_2) * 3


result_int = variant_int(var_int_1=10, var_int_2=2)
print(result_int)

result_str = variant_str(var_str_1="YES ", var_str_2="NO ")
print(result_str)
