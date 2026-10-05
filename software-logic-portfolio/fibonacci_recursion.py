# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:42:30 2024

@author: José Alberto Rocha Munguía
"""
import time

# Fibonacci sequence using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive call: sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Calculation parameters
target_number = 35 # Reduced for performance; 50 might take a long time to compute
start_time = time.time()

print(f"The Fibonacci sequence result for {target_number} is {fibonacci(target_number)}")

end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f}s")