# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:58:35 2024

@author: José Alberto Rocha Munguía
"""

"""
Binary search demo (DSA coursework).

Sorts a fixed list, then searches for a target with classic binary search
(returns on the first match).

Quick test:
  /opt/anaconda3/bin/python3 binary_search.py
  Expect sorted list and: Element 8 was found at position 9
  (list has two 8s; binary search returns the mid hit, here index 9)
"""


def binary_search(arr, goal):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == goal:
            return f"Element {goal} was found at position {mid}"
        if arr[mid] < goal:
            start = mid + 1
        else:
            end = mid - 1

    return f"Value {goal} was not found"


big_list = [5, 14, 11, 8, 6, 2, 9, 4, 8, 2, 1, 5, 7]
big_list.sort()

print("Sorted list:")
print(big_list)

target = 8
print(binary_search(big_list, target))
