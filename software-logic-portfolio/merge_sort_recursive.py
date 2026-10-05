# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:49:41 2024

@author: José Alberto Rocha Munguía
"""
import random

def merge_sort(A):
    """
    Sorts a list using the Merge Sort algorithm.
    """
    n = len(A)
    if n > 1:
        # Finding the midpoint of the list 
        mid = n // 2 
        # Dividing the list into two halves
        left_half = A[:mid]
        right_half = A[mid:]
        
        # Recursive calls for both halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Initializing indices to traverse each half and the main list
        # i: left, j: right, k: original
        i = 0
        j = 0
        k = 0
        
        # Combining the two halves into a single sorted list
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1
        
        # Adding remaining elements from the left half
        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1
            
        # Adding remaining elements from the right half
        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1

# --- Usage Example ---
# Array with random numbers to test performance
arr = [random.randint(1, 500) for i in range(30000)]
merge_sort(arr)

print("Sorted list using Merge Sort: \n", arr)