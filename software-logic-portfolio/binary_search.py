# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:58:35 2024

@author: José Alberto Rocha Munguía
"""

def binary_search(arr, goal):
    # Define start and end points
    start = 0
    end = len(arr) - 1
    count = 0
    indices = []
    
    while start <= end:
        # Calculate the middle element index
        mid = (start + end) // 2
        
        # Compare the middle element with the goal
        if arr[mid] == goal:
            count += 1
            indices.append(mid)
            # Binary search typically returns after finding one instance.
            # To find all occurrences, specialized logic is needed.
            return f"Element {goal} was found at position {mid}"
            
        elif arr[mid] < goal:
            # Adjust start to search in the right half
            start = mid + 1 
        else:
            # Adjust end to search in the left half
            end = mid - 1
            
    return f"Value {goal} was not found"

# Main execution
big_list = [5, 14, 11, 8, 6, 2, 9, 4, 8, 2, 1, 5, 7]
big_list.sort()

print("Sorted list:")
print(big_list)  

target = 8
print(binary_search(big_list, target))