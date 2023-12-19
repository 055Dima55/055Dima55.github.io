"""  1) Створіть клас Студент,
в ньому обявіть дві змінні імя де збережети імя студента,
та список його оцінок.створіть два метода в цьому класі,
перший метод який буде вітатись і при вітання використовувати імя студента.
другий метод буде виводити оцінки. Методи виводять результат через прінти. """


class Student:
    name = "Danil"
    grade = 9, 10, 8, 12

    def hello_name(self: str):
        print(f"Привіт мене звуть {self.name}")

    def my_grades(self: int):
        print(f"Це мої оцінки {self.grade}")


student_1 = Student()
student_1.hello_name()
student_1.my_grades()

student_2 = Student()
student_2.name = "Dima"
student_2.grade = 7, 12, 7, 10
student_2.hello_name()
student_2.my_grades()
