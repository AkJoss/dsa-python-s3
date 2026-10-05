# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:20:01 2024

@author: José Alberto Rocha Munguía
"""
import random

# Initializing variables
pokemon_list = []
counter = 0

# Filling the list with a random number of elements
for i in range(random.randint(1, 20)):
    pokemon_list.append(random.randint(0, 30))
    counter += 1
    
print(f"List content: {pokemon_list}")
print(f"The array size is: {counter}")
print()

def get_list_size(data_list):
    """
    Function that calculates size by popping elements 
    one by one until the list is empty.
    """
    count = 0
    running = True
    
    if not data_list:
        return 0
    else:
        while running:
            data_list.pop(0) # Removes the first element
            count += 1
            if not data_list:
                running = False
    return count

# Calling the function with the generated list
print(f"Size calculated by function: {get_list_size(pokemon_list)}")
