# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:06:15 2024

@author: José Alberto Rocha Munguía
"""

"""
Linear search demo (DSA coursework).

Quick test:
  python3 linear_search.py
  Expect: The searched value 8 was found 2 time(s) at positions [3, 8]
"""


def linear_search(arr, goal):
    count = 0
    indices = []
    for i in range(len(arr)):
        if arr[i] == goal:
            count += 1
            indices.append(i)

    if count == 0:
        return f"Value {goal} was not found"
    return f"The searched value {goal} was found {count} time(s) at positions {indices}"


big_list = [5, 14, 11, 8, 6, 2, 9, 4, 8, 2, 1, 5, 7]
target = 8
print(linear_search(big_list, target))

