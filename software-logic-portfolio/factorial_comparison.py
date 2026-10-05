# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:13:23 2024

@author: José Alberto Rocha Munguía
"""
import time
import sys

# Increase the recursion limit for large numbers like 1558
sys.setrecursionlimit(2000)

# Factorial without recursion
def factorial_1(n):
    tamal = 1
    for i in range(2, n + 1):
        tamal = tamal * i 
    return tamal

# Factorial with recursion
def factorial_2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_2(n - 1)

# Usage example
numerito = 15
start_time = time.time()

print(f"The factorial of {numerito} is {factorial_2(numerito)}")

end_time = time.time()
print(f"Execution time: {end_time - start_time}s")