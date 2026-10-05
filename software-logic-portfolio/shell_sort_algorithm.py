# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:48:35 2024

@author: José Alberto Rocha Munguía
"""
import random

def shell_sort(A):
    """
    Sorts a list using the Shell Sort algorithm.
    """
    # Initialize the size of the list
    n = len(A)
    # Start with an interval equal to half the size of the list
    gap = n // 2
    
    # Continue reducing the interval until it reaches 0
    while gap > 0:
        # Traverse the list from the gap index to the end
        for i in range(gap, n):
            # Save the current value in a temporary variable
            temp = A[i]
            # Initialize the variable j at position i
            j = i
            
            # Shift elements of the sorted subarray 
            # if they are greater than the temporary value
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            
            # Insert the temporary value in its correct position
            A[j] = temp
            
        # Reduce the gap
        gap //= 2
        
# --- Usage Example ---
# Array with random numbers to test performance
arr = [random.randint(1, 500) for i in range(30000)]
shell_sort(arr)
print("Sorted list using Shell Sort: ", arr)