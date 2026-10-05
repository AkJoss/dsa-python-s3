# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:49:41 2024

@author: José Alberto Rocha Munguía
"""

"""
Recursive merge sort demo (DSA coursework).

Quick test:
  python3 merge_sort_recursive.py
  Expect a confirmation that 30000 random ints are sorted (prints sample, not all).
"""

import random


def merge_sort(A):
    """In-place merge sort."""
    n = len(A)
    if n > 1:
        mid = n // 2
        left_half = A[:mid]
        right_half = A[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1


arr = [random.randint(1, 500) for _ in range(30000)]
merge_sort(arr)
ok = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
print(f"Merge sort done. n={len(arr)}, sorted={ok}, first5={arr[:5]}, last5={arr[-5:]}")

