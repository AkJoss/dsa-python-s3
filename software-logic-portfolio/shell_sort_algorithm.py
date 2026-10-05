# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:48:35 2024

@author: José Alberto Rocha Munguía
"""

"""
Shell sort demo (DSA coursework).

Quick test:
  python3 shell_sort_algorithm.py
  Expect confirmation that 30000 random ints are sorted (sample print).
"""

import random


def shell_sort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        gap //= 2


arr = [random.randint(1, 500) for _ in range(30000)]
shell_sort(arr)
ok = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
print(f"Shell sort done. n={len(arr)}, sorted={ok}, first5={arr[:5]}, last5={arr[-5:]}")

