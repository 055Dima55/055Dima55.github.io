'''Зробіть словник де буде табличка множення додавання ділення
і віднімання чисел від 2 до 9(включно). (так як робили на уроці).
Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
Коли ви підготуєте це, запитайте в користувача
яку табличку він хоче побачити (додавання, віднімання, множення, ділення). і виведіть йому цю табличку. '''

#for i in range(2, 10):
#    for j in range(2, 10):
#        print(f"{i}-{j}={i-j}", end=" ")
#    print()



addition_table = {}
for i in range(2, 10):
    addition_table[i] = {}
    for j in range(2, 10):
        addition_table[i][j] = i + j

multiplication_table = {}
for i in range(2, 10):
    multiplication_table[i] = {}
    for j in range(2, 10):
        multiplication_table[i][j] = i * j

subtraction_table = {}
for i in range(2, 10):
    subtraction_table[i] = {}
    for j in range(2, 10):
        subtraction_table[i][j] = i - j

division_table = {}
for i in range(2, 10):
    division_table[i] = {}
    for j in range(2, 10):
        division_table[i][j] = i / j


operation = input("Виберіть операцію { +, -, *, / } ")

if operation == "+":
    for i in range(2, 10):
        for j in range(2, 10):
            print(f"{i} + {j} = {addition_table[i][j]}", end=" ")
        print()

elif operation == "-":
    for i in range(2, 10):
        for j in range(2, 10):
            print(f"{i} - {j} = {subtraction_table[i][j]}", end=" ")
        print()

elif operation == "*":
    for i in range(2, 10):
        for j in range(2, 10):
            print(f"{i} * {j} = {multiplication_table[i][j]}", end=" ")
        print()

elif operation == "/":
    for i in range(2, 10):
        for j in range(2, 10):
            print(f"{i} / {j} = {division_table[i][j]}", end=" ")
        print()
else:
    print("Немає такої операції")
