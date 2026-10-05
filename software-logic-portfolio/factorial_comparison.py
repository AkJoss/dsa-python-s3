# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:13:23 2024

@author: José Alberto Rocha Munguía
"""

"""
Iterative vs recursive factorial demo (DSA coursework).

Quick test:
  python3 factorial_comparison.py
  Expect factorial of 15 = 1307674368000 and an execution time line.
"""

import time
import sys

sys.setrecursionlimit(2000)


def factorial_1(n):
    """Iterative factorial."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_2(n):
    """Recursive factorial."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_2(n - 1)


numerito = 15
start_time = time.time()
print(f"The factorial of {numerito} is {factorial_2(numerito)}")
end_time = time.time()
print(f"Execution time: {end_time - start_time}s")

