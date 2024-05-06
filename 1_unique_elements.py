from typing import List
import unittest
'''
Написать функцию, которая принимает на вход список
целых чисел и возвращает новый список, содержащий
только уникальные элементы из исходного списка
'''

def get_unique_elements_without_preserved_order(items: List[int]) -> List[int]:
    """функция, которая возвращает список, содержащий
     только уникальные элементы, при этом порядок элементов не сохраняется"""
    items_set = set(items)
    result = list(items_set)
    return result

def get_unique_elements_with_preserved_order(items: List[int]) -> List[int]:
    """функция, которая возвращает список, содержащий
     только уникальные элементы, при этом порядок элементов сохраняется"""
    j = 0
    for i in range(1, len(items)):
        if items[j] != items[i]:
            j += 1
            items[j] = items[i]
    return items[:j + 1]

class UniqueElementsWithoutPreservedOrderTestCase(unittest.TestCase):
    def test_correct(self):
        #проверка отсутствия дубликатов в списке, возвращаемом функцией get_unique_elements_without_preserved_order
        test_list = [1, 2, 3, 4, 4, 2]
        result = get_unique_elements_without_preserved_order(test_list)
        self.assertEqual(sorted(result), [1, 2, 3, 4])
        #проверка работы функции get_unique_elements_without_preserved_order с пустым списком
        test_list = []
        result = get_unique_elements_without_preserved_order(test_list)
        self.assertEqual(result, [])

class UniqueElementsWithPreservedOrderTestCase(unittest.TestCase):
    def test_correct(self):
        # проверка отсутствия дубликатов и сохранения порядка в списке, возвращаемом функцией get_unique_elements_with_preserved_order
        test_list = [1, 1, 3, 4, 4, 2]
        result = get_unique_elements_with_preserved_order(test_list)
        self.assertEqual(result, [1, 3, 4, 2])
        # проверка работы функции get_unique_elements_with_preserved_order с пустым списком
        test_list = []
        result = get_unique_elements_with_preserved_order(test_list)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()