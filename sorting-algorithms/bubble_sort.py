# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:44:02 2024

@author: José Alberto Rocha Munguía
"""
import time
import random

def Bubble_Sort(arr):
    n = len(arr)
    for i in range(n-1):
        # print(f"Pass,", i)
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap
                # print (arr)
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
                # print(f"Swapping {arr[j]} for {arr[j+1]}")
                # print (arr)
        # print(f"End of pass,", i)
    return arr

# Usage example
# arr = [5, 3, 8, 4, 2]
arr = [random.randint(1, 100) for i in range(50000)]

# Measure execution time
start_time = time.time()
print(Bubble_Sort(arr))

# Finished sorting the array
end_time = time.time()

# Show execution time
print(f"Sorting {len(arr)} numbers takes:\n ")
print("Execution time: {:.9f} seconds".format(end_time - start_time))