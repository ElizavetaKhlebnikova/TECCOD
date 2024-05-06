import unittest
from typing import List
'''
Написать функцию, которая принимает на вход два целых числа (минимум и максимум)
и возвращает список всех простых чисел в заданном диапазоне
'''

def get_numeric_range(minimum: int, maximum: int) -> List[int]:
    """функция, которая возвращает список, содержащий
     все простые числа в заданном диапазоне"""
    return list(range(minimum, maximum))


class GetNumericRangeTestCase(unittest.TestCase):
    def test_correct(self):
        #проверяет правильность диапазона при передаче положительных чисел
        result = get_numeric_range(0, 10)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(result, expected)
        # проверяет правильность диапазона при передаче отрицательных чисел
        result = get_numeric_range(-10, 0)
        expected = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()