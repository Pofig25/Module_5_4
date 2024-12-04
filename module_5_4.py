class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors =  number_of_floors

#    def go_to(self, new_floor):
#        for i in range(1, new_floor + 1):
#            if 1 <= new_floor <= self.number_of_floors:
#                print(i)
#            else:
#                print('Такого этажа не существует')
#                break

#    def __len__(self):
#        return (self.number_of_floors)

#    def __str__(self):
#        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

#    def __eq__(self, other):
#        if isinstance(other.number_of_floors, int) and isinstance(other, House):
#            return self.number_of_floors == other.number_of_floors

#    def __add__(self, value):
#        if isinstance(value, int):
#            self.number_of_floors += value
#            return self

#    def __iadd__(self, value):
#        if isinstance(value, int):
#            self.number_of_floors += value
#            return self

#    def __radd__(self, value):
#        if isinstance(value, int):
#            self.number_of_floors += value
#            return self

#    def __gt__(self, other):
#        if isinstance(other.number_of_floors, int) and isinstance(other, House):
#            return self.number_of_floors > other.number_of_floors

#    def __ge__(self, other):
#        if isinstance(other.number_of_floors, int) and isinstance(other, House):
#            return self.number_of_floors >= other.number_of_floors

#    def __lt__(self, other):
#        if isinstance(other.number_of_floors, int) and isinstance(other, House):
#            return self.number_of_floors < other.number_of_floors

#    def __le__(self, other):
#        if isinstance(other.number_of_floors, int) and isinstance(other, House):
#            return self.number_of_floors <= other.number_of_floors

#    def __ne__(self, other):
#        if isinstance(other.number_of_floors, int) and isinstance(other, House):
#            return self.number_of_floors != other.number_of_floors

    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'Дом в {self.name} снесён, но он останется в истории')

# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)

# h1.go_to(5)
# h2.go_to(10)

# __str__
# print(h1)
# print(h2)

# __len__
# print(len(h1))
# print(len(h2))

# print(h1==h2)

# h1 = h1 + 10
# print(h1)
# print(h1 == h2)

# h1 += 10
# print(h1)

# h2 = 10 + h2
# print(h2)

# print(h1 > h2)
# print(h1 >= h2)
# print(h1 < h2)
# print(h1 <= h2)
# print(h1 != h2)
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)

'''
В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута
houses_history.

Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)

Вывод на консоль:
['ЖК Эльбрус']
['ЖК Эльбрус', 'ЖК Акация']
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Акация снесён, но он останется в истории
ЖК Матрёшки снесён, но он останется в истории
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Эльбрус снесён, но он останется в истории
'''