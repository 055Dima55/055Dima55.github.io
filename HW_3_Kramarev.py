
''' Задача 1

Уявимо що до нас прийшов наш друг або подруга і попросили написати додаток для покупок в магазині
що б можна було скласти список продуктів та коли купуєш викреслювати(для викреслення питайте номер елемента,
що б видалити по індексу треба його передати в pop list_a.pop(0) - видалить нульовий індекс, памятайте що користувач
не знає що в нас індекси починаються з нуля)Також нам відомо що цей список має пять або більше елементів.
Після кожного видалення елементу виводьте наш оновлений список.
Після 5 видалень перевірте чи список пустий якщо не пустий напишіть що ось ще є продукти, якщо пусти то напишіть про це.
Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик. і виведіть їх на екран.
Але цього разу вже без видалень.
кроки:
    Спочатку пропонуємо користувачу ввести продукти.
    Робимо 5 запитів на видалення
    Перевіряємо корзину
    Пропонуємо додати продукти
    Виводмо список і прощаємось '''


products_1 = input("Введіть список продуктів ")
print(products_1)
basket_product = products_1.split()

index_removed_product_1 = int(input("Вкажіть номер продукта який треба прибрати ")) - 1
if 0 <= index_removed_product_1 < len(basket_product):
    removed_product_1 = basket_product.pop(index_removed_product_1)
    print("Прибрали продукт", removed_product_1, " в карзині залишается")
    print(basket_product)
else:
    print("У вас немае стільки продуктів")

index_removed_product_2 = int(input("Вкажіть номер продукта який треба прибрати ")) - 1
if 0 <= index_removed_product_1 < len(basket_product):
    removed_product_2 = basket_product.pop(index_removed_product_1)
    print("Прибрали продукт", removed_product_2, " в карзині залишается")
    print(basket_product)
else:
    print("У вас немае стільки продуктів")

index_removed_product_3 = int(input("Вкажіть номер продукта який треба прибрати ")) - 1
if 0 <= index_removed_product_1 < len(basket_product):
    removed_product_3 = basket_product.pop(index_removed_product_1)
    print("Прибрали продукт", removed_product_3, " в карзині залишается")
    print(basket_product)
else:
    print("У вас немае стільки продуктів")

index_removed_product_4 = int(input("Вкажіть номер продукта який треба прибрати ")) - 1
if 0 <= index_removed_product_1 < len(basket_product):
    removed_product_4 = basket_product.pop(index_removed_product_1)
    print("Прибрали продукт", removed_product_4, " в карзині залишается")
    print(basket_product)
else:
    print("У вас немае стільки продуктів")

index_removed_product_5 = int(input("Вкажіть номер продукта який треба прибрати ")) - 1
if 0 <= index_removed_product_1 < len(basket_product):
    removed_product_5 = basket_product.pop(index_removed_product_1)
    print(f"Прибрали продукт", removed_product_5, " в карзині залишается")

print( "В кошику зараз")
print(basket_product)


products_2 = input("Продукти які треба додати, може ви щось забули")
basket_product.append(products_2)

print("Ось ваші продукти, гарного дня")
print(basket_product)