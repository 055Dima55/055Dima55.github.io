'''
1) Напишіть ліст компрехеншин який
 формує список всіх чисел від 34 до 121 які діляться націло на 3 та на 2
2) Напишіть клас калькулятора де будуть 4 арифметичні дії
 плюс, мінус, додавання, множення - звичайні методи.
і зробіть статік метод який буде виводити повідомлення,
 привіт я калькулятор.
'''

# 1)
list_a = [i for i in range(34, 121, 1) if i % 3 == 0 and i % 2 == 0]
print(list_a)


# 2)
class Calculator:
    def addition(self, x, y):
        result = x + y
        return result

    def subtracting(self, x, y):
        result = x - y
        return result

    def multiply(self, x, y):
        result = x * y
        return result

    def division(self, x, y):
        if y != 0:
            result = x / y
            return result
        else:
            return "Не ділимо на 0"

    @staticmethod
    def greet():
        return "Привіт я калькулятор"


calk = Calculator()
print(Calculator.greet())
print(calk.addition(10, 20))
print(calk.subtracting(10, 5))
print(calk.multiply(2, 4))
print(calk.division(10, 2))
print(calk.division(5, 0))
