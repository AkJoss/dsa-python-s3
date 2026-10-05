# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:09:54 2024

@author: José Alberto Rocha Munguía
"""

def divide_and_conquer(data_list, target):
    """
    Finds an element in a sorted list using the Divide and Conquer strategy.
    """
    # Base case: If the list is empty, return -1
    if not data_list:
        return -1
    
    # Calculate the midpoint of the list
    mid = len(data_list) // 2
    
    # Verify if the element is at the midpoint
    if data_list[mid] == target:
        return mid
    
    # If target is greater, search in the right half
    elif data_list[mid] < target:
        right_half = data_list[mid + 1:]
        # Recursively search in the right sublist
        sub_result = divide_and_conquer(right_half, target)
        
        # If found in the right half, adjust index relative to the original list
        if sub_result != -1:
            return mid + 1 + sub_result
        else:
            return -1
            
    # If target is smaller, search in the left half
    else:
        left_half = data_list[:mid]
        return divide_and_conquer(left_half, target)

# --- Usage Example ---
# Remember: The list must be sorted for binary search to work.
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
target_value = 11

result_index = divide_and_conquer(numbers, target_value)

# Print results
if result_index != -1:
    print(f"Element {target_value} is at index: {result_index}")
else:
    print(f"Element {target_value} was not found in the list")