# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:08:34 2024

@author: José Alberto Rocha Munguía
"""
import random
import time

def Insertion_Sort(arr):
    n = len(arr)
    for i in range(1, n-1):
        aux = arr[i]
        j = i - 1
        while j >= 0 and aux < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = aux
    return arr
    
# Usage example
# arr = [5, 3, 8, 4, 2]
arr = [random.randint(1, 100) for i in range(50000)]

# Measure execution time
start_time = time.time()
print(Insertion_Sort(arr))

# Finished sorting the array
end_time = time.time()

# Show execution time
print(f"Sorting {len(arr)} numbers takes:\n ")
print("Execution time: {:.6f} seconds".format(end_time - start_time))