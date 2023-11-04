# class Point:
#     '''Описание работы класса'''
#     color = 'red'
#     circle = 2
import random


# class Book:
#
#     def __init__(self, name, author, isbn):
#         self.__name = name
#         self.__author = author
#         self.__isbn = isbn
#     def get_auther(self):
#         return self.__author
#     def set_author(self, author):
#         self.__author = author
#     def get_name(self):
#         print(self.__name)
#     def set_name(self, name):
#         self.__name = name
#     def get_isbn(self):
#         return self.__isbn
#     def set_isbn(self, isbn):
#         self.__isbn = isbn
#
# b = Book('name', 'author1', 12345)
# print(b.get_auther())
# b.set_author('QwE')
# print(b.get_auther())
# b.set_name('dcxsfvfhnbmjk')
# b.get_name()
# t = (b.get_auther())
# print(t*3)

# class Figure:
#     def __init__(self, coords, width, color):
#         self.coords = coords
#         self.width = width
#         self.color = color
#     def draw(self):
#         print(f'Рисуем фигуру цветом {self.color} и шириной  {self.width}')
# class Line(Figure):
#     def draw(self):
#         print(f'Рисуем линию цветом {self.color} и шириной  {self.width}')
#     def del_line(self):
#         print('линия удалена')
#
# class Rect(Figure):
#     def __init__(self, coords, width, color, right):
#         super().__init__(coords, width, color)
#         self.right = right
#
#     def draw(self):
#         print(f'Рисуем примоугольник цветом {self.color} и шириной  {self.width}. Прямоугольник {self.right}')
#
#
# class Ellips(Figure):
#     def draw(self):
#         print(f'Рисуем эллипс цветом {self.color} и шириной  {self.width}')
#
#
# f = Figure([1, 2, 4, 5, 7, 8], 2, 'black')
# f.draw()
# l = Line([1, 2, 3, 4], 3, 'red')
# l.draw()
# e = Ellips([5, 5, 2, 9], 4, 'yellow')
# e.draw()
# r = Rect([1, 8, 6, 2], 6, 'bluo', 'неправильный')
# r.draw()
# l.del_line()

# class Publication:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#
#     def display(self):
#         print('Название', self.title)
#         print(f'Автор: {self.author}')
#         print(f'Год издания {self.year}')
#
# class Book(Publication):
#     def __init__(self, title, author, year, isbn):
#         super().__init__(title, author, year)
#         self.isbn = isbn
#
#     def display(self):
#         super().display()
#         print(f'ISBN {self.isbn}')
#
# class Magazine(Publication):
#     def __init__(self, title, author, year, isbn_number):
#         super().__init__(title, author, year)
#         self.isbn_number = isbn_number
#
#     def display(self):
#         super().display()
#         print(f'ISBN {self.isbn_number}')
#
# def info(obj):
#     obj.display()
#
# p = Publication('Название 1', 'Автор 1', 1980)
# # p.display()
# # info(p)
# b = Book('Мир грёз', 'Артур Мильтер', 2003, 4567897654356789765)
# # b.display()
# # info(b)
# n = Magazine('Город СтимПанк', 'Милана Шельф', 1994, 987654567898765)
# # n.display()
# # info(n)
# list = []
# list.append(p)
# list.append(b)
# list.append(n)
# for i in list:
#     info(i)
#     print()

# class MusicAlbum:
#     def __init__(self, title, artist, release_year, ganre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.ganre = ganre
#         self.tracklist = tracklist
#
#     def get_info(self):
#         print(f'''
# Название: {self.title}
# Исполнитель: {self.artist}
# год выпуска: {self.release_year}
# Жарн: {self.ganre}
# Список треков: {self.tracklist}''')
#     def play_random_track(self):
#         return random.choice(self.tracklist)
#
#
# album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
#                     ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
#                      "Hallomann"])
# album4.get_info()
# print(album4.play_random_track())

# class Student:
#     def __init__(self, name, age, grade, scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def info(self):
#         print(f'Имя: {self.name}')
#         print(f'Возраст: {self.age}')
#         print(f'Класс: {self.grade}')
#         print(f'Оценки: {self.scores}')
#     def average_score(self):
#         return sum(self.scores) / len(self.scores)
#
# student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
# student2.info()
# print(f'Средний балл: {student2.average_score()}')

# class Recipe:
#     def __init__(self, name, ingredients):
#         self.name = name
#         self.ingredients = ingredients
#     def print_ingredients(selfs):
#         print(f'Ингредиенты для {selfs.name}')
#         for i in selfs.ingredients:
#             print('-', i)
#
#     def cook(self):
#         print(f'Сегодня мы готовим {self.name} \nВыполняем инструкцию по приготовлению блюда {self.name}... \nБлюдо {self.name} готово! ')
#
# # создаем рецепт спагетти болоньезе
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
#
# # печатаем список продуктов для рецепта спагетти
# spaghetti.print_ingredients()
#
# # готовим спагетти
# spaghetti.cook()
#
# # создаем рецепт для кекса
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
#
# # печатаем рецепт кекса
# cake.print_ingredients()
#
# # готовим кекс
# cake.cook()

# class Publisher:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#
#     def get_info(self):
#         print(f'Издательство {self.name}, находиться в {self.location}')
#     def publish(self, message):
#         print(f'Готовим {message} к публикации в {self.name} ({self.location})')
#
#
# class BookPublisher(Publisher):
#     def __init__(self, name, location, num_authors):
#         super().__init__(name, location)
#         self.num_authors = num_authors
#
#     def get_info(self):
#         print(f'Издательство {self.name}, находиться в {self.location}, количество авторов в издательстве {self.num_authors} ')
#     def publish(self, message, message2):
#         print(f'Передаём рукописть {message}, написаннyю автором {message2} в издательство {self.name}({self.location})')
#
#
# class NewspaperPublisher(Publisher):
#     def __init__(self, name, location, num_pages):
#         super().__init__(name, location)
#         self.num_pages = num_pages
#
#     def get_info(self):
#         print(
#             f'Издательство {self.name}, находиться в {self.location}, количество страниц в газете {self.num_pages} ')
#
#     def publish(self, message):
#         print(f'Печатаем свежий номер со статьей {message} на главной странице в издательстве {self.name}({self.location})')
#
#
#
# publisher = Publisher("АБВГД Пресс", "Москва")
# publisher.publish('"Справочник писателя"')
#
# book_publisher = BookPublisher("Важные Книги", "Самара", 52)
# book_publisher.publish("'Приключения Чебурашки'", "В.И. Пупкин")
#
# newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
# newspaper_publisher.publish('"Новая версия Midjourney будет платной"')

# class BankAccount:
#     def __init__(self, balance, interest_rate):
#         self.__balance = balance
#         self.__interest_rate = interest_rate
#         self.__transactions = []
#
#     def deposit(self, amount):
#         self.__balance += amount
#         self.__transactions.append(f'Внесение наличных на счет: {amount}')
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append(f'Снятие наличных: {amount}')
#         else:
#             print('На счёте недостаточно средств')
#
#     def add_interest(self):
#         interest = self.__balance * self.__interest_rate
#         self.__balance += interest
#         self.__transactions.append(f'Начислены проценты по вкладу: {interest}')
#
#     def history(self):
#         for transactions in self.__transactions:
#             print(transactions)
#
# # создаем объект счета с балансом 100000 и процентом по вкладу 0.05
# account = BankAccount(100000, 0.05)
#
# # вносим 15 тысяч на счет
# account.deposit(15000)
#
# # снимаем 7500 рублей
# account.withdraw(7500)
#
# # начисляем проценты по вкладу
# account.add_interest()
#
# # печатаем историю операций
# account.history()

# class Employee:
#     def __init__(self, name, age, salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_bonus(self, bonus):
#         self.__bonus = bonus
#
#     def get_bonus(self):
#         return self.__bonus
#
#     def get_total_salary(self):
#         return self.__salary + self.__bonus
#
#
# # создаем сотрудника с именем, возрастом и зарплатой
# employee = Employee("Марина Арефьева", 30, 90000)
#
# # устанавливаем бонус для сотрудника
# employee.set_bonus(15000)
#
# # выводим имя, возраст, зарплату, бонус и общую зарплату сотрудника
# print("Имя:", employee.get_name())
# print("Возраст:", employee.get_age())
# print("Зарплата:", employee.get_salary())
# print("Бонус:", employee.get_bonus())
# print("Итого начислено:", employee.get_total_salary())

# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs
#
#     def info(self):
#         print(f'Кличка {self.name}, вид {self.species}, количество ног {self.legs}')
#
#     def voice(self):
#         print(f'{self.name} подает голос')
#
#     def move(self):
#         print(f'{self.name} дергает хвостом')
#
# class Dog(Animal):
#     def __init__(self, name, breed, legs):
#         super().__init__(name, [], legs)
#         self.breed = breed
#
#     def bark(self):
#         print(f'{self.breed} {self.name} лает')
#
# class Bird(Animal):
#     def __init__(self, name, breed, legs):
#         super().__init__(name, [], legs)
#         self.breed = breed
#
#     def fly(self):
#         print(f'{self.breed} {self.name} летает')
#
# dog = Dog("Геральт", "доберман", 4)
# bird = Bird("Вася", "попугай", 2)
# dog.voice()
# bird.voice()
# dog.move()
# bird.move()
# dog.bark()
# bird.fly()

# import math
# class Shape:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def describe(self):
#         print(f'Геометрическая фигура {self.name}, цвет фигуры {self.color}')
#
# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__([], color)
#         self.radius = radius
#
#     def area(self):
#
#         return round((self.radius ** 2 * math.pi), 1)
#
#
#     def describe(self):
#         print(f'Это геометрическая фигура, цвет-{self.color}.')
#         print(f'Это окружность. Радиус-{self.radius} см, цвет-{self.color}.')
# class Rectangle(Shape):
#     def __init__(self, color, length, width):
#         super().__init__([], color)
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def describe(self):
#         print(f'Это геометрическая фигура, цвет-{self.color}.')
#         print(f'Это {self.color} прямоугольник. Длина-{self.length} см, ширина-{self.width} см.')
#
# class Triangle(Shape):
#     def __init__(self, color, base, heigth):
#         super().__init__([], color)
#         self.base = base
#         self.heigth = heigth
#
#     def area(self):
#         return self.base * self.heigth * 0.5
#
#     def describe(self):
#         print(f'Это геометрическая фигура, цвет-{self.color}.')
#         print(f'Это {self.color} треугольник с основанием {self.base} см и высотой {self.heigth} см.')
#
# circle = Circle("красный", 5)
# rectangle = Rectangle("синий", 3, 4)
# triangle = Triangle("фиолетовый", 6, 8)
# circle.describe()
# rectangle.describe()
# triangle.describe()
# print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")

# class Candy:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
# class Chocolate(Candy):
#     def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
#         super().__init__(name, price, weight)
#         self.chocolate_type = chocolate_type
#         self.cocoa_percentage = cocoa_percentage
#
# class Gummy(Candy):
#     def __init__(self, name, price, weight, flavor, shape):
#         super().__init__(name, price, weight)
#         self.flavor = flavor
#         self.shape = shape
#
# class HardCandy(Candy):
#     def __init__(self, name, price, weight, flavor, filled):
#         super().__init__(name, price, weight)
#         self.flavor = flavor
#         self.filled = filled
#
# chocolate = Chocolate(name="Швейцарские луга", price=325.50, weight=220, cocoa_percentage=40, chocolate_type="молочный")
# gummy = Gummy(name="Жуй-жуй", price=76.50, weight=50, flavor="вишня", shape="медведь")
# hard_candy = HardCandy(name="Crazy Фрукт", price=35.50, weight=25, flavor="манго", filled=True)
#
# print("Шоколадные конфеты:")
# print(f"Название конфет: {chocolate.name}")
# print(f"Стоимость: {chocolate.price} руб")
# print(f"Вес брутто: {chocolate.weight} г")
# print(f"Процент содержания какао: {chocolate.cocoa_percentage}")
# print(f"Тип шоколада: {chocolate.chocolate_type}")
# print("\nМармелад жевательный:")
# print(f"Название конфет: {gummy.name}")
# print(f"Стоимость: {gummy.price} руб")
# print(f"Вес брутто: {gummy.weight} г")
# print(f"Вкус: {gummy.flavor}")
# print(f"Форма: {gummy.shape}")
# print("\nФруктовые леденцы:")
# print(f"Название конфет: {hard_candy.name}")
# print(f"Стоимость: {hard_candy.price} руб")
# print(f"Вес брутто: {hard_candy.weight} г")
# print(f"Вкус: {hard_candy.flavor}")
# print(f"Начинка: {hard_candy.filled}")

# class Soldier:
#     def __init__(self, name, rank, service_number):
#         self.name = name
#         self.__rank = rank
#         self.__service_number = service_number
#
#
#     def info(self):
#         # print(f"'Создан новый игровой персонаж типа Soldier с атрибутами: 'name': '{self.name}', '_Soldier__rank': '{self.__rank}', '_Soldier__service_number': '{self.__service_number}'")
#         print('Создан новый игровой персонаж типа Soldier с атрибутами: ', "{'name':", f"'{self.name}'", "'_Soldier__rank':", f"'{self.__rank}'", "'_Soldier__service_number':", f"'{self.__service_number}'"'}')
#
#     def get_rank(self):
#         print(f'Персонаж {self.name} имеет звание {self.__rank}')
#
#     def promote(self):
#         print(f'{self.name} повышен в звании, он теперь ефрейтор')
#
#     def demote(self):
#         print(f'{self.name} понижен в звании, он теперь {self.__rank}')
#
#
#
# soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
# soldier1.info()
# soldier1.get_rank()
# soldier1.promote()
# soldier1.demote()
