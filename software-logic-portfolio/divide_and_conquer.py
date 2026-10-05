# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:09:54 2024

@author: José Alberto Rocha Munguía
"""

"""
Divide-and-conquer search demo (DSA coursework).

Recursive binary-style search on a sorted list (splits left/right halves).

Quick test:
  /opt/anaconda3/bin/python3 divide_and_conquer.py
  Expect: Element 11 is at index: 4
"""


def divide_and_conquer(data_list, target):
    """Find target in a sorted list; return index or -1."""
    if not data_list:
        return -1

    mid = len(data_list) // 2

    if data_list[mid] == target:
        return mid

    if data_list[mid] < target:
        right_half = data_list[mid + 1:]
        sub_result = divide_and_conquer(right_half, target)
        if sub_result != -1:
            return mid + 1 + sub_result
        return -1

    left_half = data_list[:mid]
    return divide_and_conquer(left_half, target)


# List must be sorted for this search to work
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
target_value = 11

result_index = divide_and_conquer(numbers, target_value)

if result_index != -1:
    print(f"Element {target_value} is at index: {result_index}")
else:
    print(f"Element {target_value} was not found in the list")
