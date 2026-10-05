# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:08:34 2024

@author: José Alberto Rocha Munguía
"""

"""
Insertion sort implementation (DSA coursework).

Import Insertion_Sort from other scripts, or run this file for a timed demo.

Quick test:
  python3 insertion_sort.py
  Expect sorted=True and an execution-time line (demo uses 5000 ints).
"""
import random
import time


def Insertion_Sort(arr):
    """Sort arr in ascending order with insertion sort; return the same list."""
    n = len(arr)
    for i in range(1, n):
        aux = arr[i]
        j = i - 1
        while j >= 0 and aux < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = aux
    return arr


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(5000)]
    start_time = time.time()
    Insertion_Sort(arr)
    end_time = time.time()
    ok = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    print(f"Insertion sort done. n={len(arr)}, sorted={ok}")
    print("Execution time: {:.6f} seconds".format(end_time - start_time))
