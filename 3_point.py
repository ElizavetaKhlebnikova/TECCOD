from math import sqrt
import unittest

"""
Создать класс Point, который представляет собой точку в двумерном пространстве. 
Класс должен иметь методы для инициализации координат точки, вычисления расстояния
до другой точки, а также для получения и изменения координат.
"""


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if isinstance(x, int):
            self._x = x
        else:
            raise ValueError('Передано некорректное значение x')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if isinstance(y, int):
            self._y = y
        else:
            raise ValueError('Передано некорректное значение y')

    def get_distance(self, other) -> int:
        if isinstance(other, self.__class__):
            distance = sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))
            return distance
        raise ValueError('Передано некорректное значение второй точки, требуется передать экземпляр класса Point')

    def get_coordinats(self) -> tuple:
        return self.x, self.y

    def set_coordinats(self, x=None, y=None) -> None:
        if x != None:
            self.x = x
        if y != None:
            self.y = y


class PointTestCase(unittest.TestCase):
    def test_changing_coordinates(self):
        #проверка корректности создания экземпляра класса Point
        point = Point(1, 2)
        self.assertEqual((point.x, point.y), (1, 2))
        #проверка изменения координаты х экземпляра класса Point
        point.set_coordinats(x=3)
        self.assertEqual((point.x, point.y), (3, 2))
        #проверка изменения координаты у экземпляра класса Point
        point.set_coordinats(y=4)
        self.assertEqual((point.x, point.y), (3, 4))
        #проверка возбуждений исключения при передаче нечислового аргумента экземпляру класса Point
        self.assertRaises(ValueError, point.set_coordinats, 'a', 1)
        self.assertRaises(ValueError, point.set_coordinats, 1, 'b')
        #проверка корректности работы методов по получению и изменению координат экземпляра класса Point
        point.set_coordinats(0, 0)
        self.assertEqual(point.get_coordinats(), (0, 0))

    def test_get_distance(self):
        #проверка корректности работы функции get_distance класса Point
        point1 = Point(3, 2)
        point2 = Point(7, 8)
        result = round(point1.get_distance(point2), 2)
        self.assertEqual(result, 7.21)
        #проверка изменения результата при смене координат одного из экземпляров класса Point
        point2.set_coordinats(y=7)
        result = round(point1.get_distance(point2), 2)
        self.assertEqual(result, 6.4)
        #проверка возбуждения исключения при передаче в функцию get_distance класса Point неверного аргумента
        self.assertRaises(ValueError, point1.get_distance, 1)

