import math
from datetime import date, datetime

# класс Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# класс Person 
class Person:
    def __init__(self, name, nationality, birth_date_str):
        self.name = name
        self.nationality = nationality
        self.birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

# класс Calculator
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Ошибка: Деление на ноль невозможно"
        return a / b

#использование
if __name__ == "__main__":
    # проверка Circle
    radius = 5
    my_circle = Circle(radius)
    print(f"Радиус: {radius}")
    print(f"Площадь: {my_circle.calculate_area():.2f}")
    print(f"Периметр: {my_circle.calculate_perimeter():.2f}")
    print()

    # проверка Person
    person = Person("Роман Михайлов", "Русский", "2007-05-25")
    print(f"Имя: {person.name}")
    print(f"Национальность: {person.nationality}")
    print(f"Возраст: {person.calculate_age()} лет")
    print()

    # проверка Calculator
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(f"10 / 0 = {calc.divide(10, 0)}")