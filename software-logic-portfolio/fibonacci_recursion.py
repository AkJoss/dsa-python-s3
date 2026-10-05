# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:42:30 2024

@author: José Alberto Rocha Munguía
"""

"""
Recursive Fibonacci demo (DSA coursework).

Quick test:
  python3 fibonacci_recursion.py
  Expect Fibonacci(35) = 9227465 and an execution time line.
  (n=35 is intentional; larger values get very slow.)
"""

import time


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


target_number = 35
start_time = time.time()
print(f"The Fibonacci sequence result for {target_number} is {fibonacci(target_number)}")
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f}s")

