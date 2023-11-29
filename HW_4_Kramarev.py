'''Задача 1

Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл, точна кількість не вказана.
Вам потрібно до вартості покупок додати 6,5 відсотки податків.
Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і потім віднімаєте
суму або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.

* завдання з зірочкою не впливає на бал. Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня,
якщо менше. то тоді просто відкидаємо копійки від ціни.'''


price_of_goods = input("Введіть вартість покупок ")
discount_coupon = input("У Вас є купон на знижку Так/Ні ").lower()

total_prise = 0
percent_discount = 10/100
cash_discount = 50


for i in price_of_goods.split():
    cost = int(i)/100 * 6.5 + int(i)
    total_prise += cost

if discount_coupon == "так":
    discount_type = input("У Вас  купон на суму/відсоток ").lower()
    if discount_type == "суму":
        cost_1 = format(total_prise - cash_discount, ".2f")
        print(cost_1)
    else:
        print(format(total_prise-(total_prise * percent_discount), ".2f"))
else:
    print(format(total_prise, ".2f"))


'''Задача 2
Переробіть задачу з попереднього уроку враховуючи ваші знання з цього уроку, використайте цикл for in або while.'''
#
#products_1 = input("Введіть список продуктів ")
#print(products_1)
#basket_product = products_1.split()
#
#for i in range(5):
#    index_removed_product = int(input("Вкажіть номер продукта який треба прибрати ")) - 1
#    if 0 <= index_removed_product < len(basket_product):
#        removed_product = basket_product.pop(index_removed_product)
#        print("Прибрали продукт", removed_product, " у кошику залишається")
#        print(basket_product)
#    else:
#        print("У вас немає стільки продуктів")
#
#print("у кошику зараз")
#print(basket_product)
#
#products_2 = input("Продукти які треба додати, може ви щось забули ")
#basket_product.append(products_2)
#
#print("Ось ваші продукти, гарного дня ")
#print(basket_product)
#
#

'''Задача 3
Напишіть програму Банкомат. Втсановіть пін код для користувача(зробимо це константою).
Запитайте в користувача Пін якщо він введе три рази не вірно то напишіть що карта заблокована.
Використовуйте цикл while.'''
#
#pin_cod = 1234
#attempt = 3
#
#while attempt > 0:
#    enter_pin = input("Введіть пін код ")
#    if  enter_pin == pin_cod:
#        print("Пін код вірний")
#        break
#    else:
#        attempt -= 1
#        print(f"Пін код не вірний. У вас є ще",{attempt}, "спроб")
#    if attempt == 0:
#        print("Карта заблокована")
#
'''Задача 4
Напишіть за допомогою f-string та format. Дві стрічки де буде підставлятись імя та вік з зміних
name = "оЛенА"
age = 21
f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
format_string = тут ваш код формата формат стрінг | повино вийти -> Я Олена, мені 21 рік
print(f_string)
print(format_string) '''
#
#name = "Андрій"
#age = 28
#
#f_string = f"Я {name}, мені {age} років"
#print(f_string)
#
#format_string = "Я {name}, мені {age} років.".format(name=name, age=age)
#print(format_string)
#