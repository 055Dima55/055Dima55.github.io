'''Задача 2
Візьміть задачу з минулого уроку(
3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма трьома методами
) модернізуйте її так що кожний раз коли ми її запускаємо те що ми туди передаєм та результат повинно записуватись в файл log.txt
Зверніть увагу на те що в файл повинно дозаписуватись, а не затератись.
Уявіть що ця функція являється легасі кодом і ви її не можете змінювати,
тому потрібно використовувати декоратор. Я хотів би бачити таку реалізацію в домашці три функції:
функція з минулого уроку
функція що записую текст
і декоратор'''


def writing_to_file(result, args):
    with open("log.txt", "a") as file:
        file.write(f"Result: {result}, Args: {args}\n")

def dek_three_numbers_text(funс):
    def wrapper(*args, **kwargs):
        result = funс(*args, **kwargs)
        writing_to_file(result, args)
        return result
    return wrapper

@dek_three_numbers_text
def three_numbers_text(number_1: int, number_2: int, number_3: int):
    result = number_1 + number_2 + number_3
    return result


numbers = three_numbers_text(10, 20, 1)
print(numbers)




