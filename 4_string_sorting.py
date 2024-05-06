from typing import List
import unittest

"""
Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
"""
def sort_list_by_length(strings: List[str]) -> List[str]:
    strings.sort(key=len, reverse=False)
    return strings

def sort_list_by_length_reverse(strings: List[str]) -> List[str]:
    strings.sort(key=len, reverse=True)
    return strings


data = input('Введите список слов через пробел:')
my_list = data.strip().split()
sort_list_by_length(my_list)
print(my_list)
sort_list_by_length_reverse(my_list)
print(my_list)

if __name__ == "main":
    main()