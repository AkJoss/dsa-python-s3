# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:44:02 2024

@author: José Alberto Rocha Munguía
"""

"""
Bubble sort implementation (DSA coursework).

Import Bubble_Sort from other scripts, or run this file for a timed demo.

Quick test:
  python3 bubble_sort.py
  Expect sorted=True and an execution-time line (demo uses 5000 ints).
"""
import random
import time


def Bubble_Sort(arr):
    """Sort arr in ascending order with bubble sort; return the same list."""
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux
    return arr


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(5000)]
    start_time = time.time()
    Bubble_Sort(arr)
    end_time = time.time()
    ok = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    print(f"Bubble sort done. n={len(arr)}, sorted={ok}")
    print("Execution time: {:.9f} seconds".format(end_time - start_time))
