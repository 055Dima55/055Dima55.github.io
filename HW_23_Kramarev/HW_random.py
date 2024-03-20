import random

print("Виберіть набори символів, які потрібно включити:")
print("1. Кирилиця")
print("2. Латинські букви")
print("3. Цифри")
print("4. Великі букви")
print("5. Маленькі букви")

options = {
    '1': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
    '2': 'АаБбВвГгДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщьЮюЯя',
    '3': '0123456789'
}

chosen_sets = input("Введіть номери наборів символів (наприклад, '123'): ")
password_length = int(input("Введіть довжину пароля: "))

alphabet = ''

for i in chosen_sets:
    if i in options:
        alphabet += options[i]

if '4' in chosen_sets:
    alphabet = alphabet.upper()

if '5' in chosen_sets:
    alphabet = alphabet.lower()

if alphabet:
    password = ""
    for _ in range(password_length):
        password += random.choice(alphabet)
    print("Ваш згенерований пароль:", password)
else:
    print("Ви не вибрали жодного набору символів")
