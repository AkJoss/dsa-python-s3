# -*- coding: utf-8 -*-
"""
Array size demo (DSA coursework).

Builds a list of random ints, prints its length with a counter, then
recalculates size by popping every element (destructive).

Note: list contents change every run (random length 1–20, values 0–30).
Both printed sizes should always match.

Quick test:
  /opt/anaconda3/bin/python3 array_counter.py
  Expect three lines: List content, The array size is: N, Size calculated by function: N
  (same N twice)

@author: José Alberto Rocha Munguía
"""
import random

pokemon_list = []
counter = 0

for _ in range(random.randint(1, 20)):
    pokemon_list.append(random.randint(0, 30))
    counter += 1

print(f"List content: {pokemon_list}")
print(f"The array size is: {counter}")
print()


def get_list_size(data_list):
    """Count elements by popping from the front until empty."""
    count = 0

    if not data_list:
        return 0

    while data_list:
        data_list.pop(0)
        count += 1
    return count


print(f"Size calculated by function: {get_list_size(pokemon_list)}")
