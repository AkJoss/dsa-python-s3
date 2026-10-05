# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:35:53 2024

@author: José Alberto Rocha Munguía
"""

class HashTable:
    def __init__(self, size):
        # Constructor method to initialize the hash table
        self.size = size
        self.table = [None] * size  # Create a list of fixed size
        
    def is_empty(self):
        # Method to check if the hash table is empty
        for i in range(self.size):
            if self.table[i] is not None: 
                return False
        return True
    
    def get_ratero_count(self):
        ratero = 0
        for i in range(self.size):
            if self.table[i] is not None:
                ratero += 1
        return ratero 
        
    def hash_function(self, key):
        # Method to calculate the index from the key
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            total = 0
            for char in key:
                total += ord(char)
            return total % self.size
            
    def add(self, key, value):
        # Method to add a key and its value to the hash table
        index = self.hash_function(key)
        self.table[index] = (key, value)
                
    def get_by_key(self, key):
        # Method to retrieve a value using its key
        index = self.hash_function(key)
        if self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
        return None
                
    def get_by_value(self, value):
        # Method to retrieve a key using its value
        for i in range(self.size):
            if self.table[i] is not None and self.table[i][1] == value:
                return self.table[i][0]
        return None

# --- Usage Example ---
hash_table = HashTable(5)

# Adding two keys that generate the same index (Collision)
hash_table.add(1, "value1") 
hash_table.add(6, "value2") 

# Retrieve values
print(f"Key 1: {hash_table.get_by_key(1)}") 
print(f"Key 6: {hash_table.get_by_key(6)}")
print(f"Total rateros: {hash_table.get_ratero_count()}")