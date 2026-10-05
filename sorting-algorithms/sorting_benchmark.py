# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:17:02 2024

@author: josea
"""

"""
Benchmark bubble sort vs insertion sort (DSA coursework).

Runs both on a random list and prints timing. After bubble sort the list is
already sorted, so insertion sort is much faster on the second pass (original
coursework behavior).

Quick test (from this folder):
  python3 sorting_benchmark.py
  Expect two timing blocks; bubble slower than insertion on the second run.
  Demo size is 8000 ints (full 50k bubble takes a long time).
"""
import random
import time

from bubble_sort import Bubble_Sort
from insertion_sort import Insertion_Sort

N = 8000
arr = [random.randint(1, 50) for _ in range(N)]
print(f"Sorting {len(arr)} numbers:\n")

print("############ BUBBLE SORT ##################")
start_time = time.time()
Bubble_Sort(arr)
end_time = time.time()
ok_bubble = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
print(f"sorted={ok_bubble}")
print("Execution time: {:.6f} seconds".format(end_time - start_time))

print("\n############ INSERTION SORT ###############")
start_time = time.time()
Insertion_Sort(arr)
end_time = time.time()
ok_ins = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
print(f"sorted={ok_ins}")
print("Execution time: {:.6f} seconds".format(end_time - start_time))
