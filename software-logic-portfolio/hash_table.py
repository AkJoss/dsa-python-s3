# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:16:29 2024

@author: José Alberto Rocha Munguía
"""

class HashTable:
    def __init__(self, size):
        # Constructor to initialize the hash table with a fixed size
        self.size = size
        self.table = [None] * size
        
    def is_empty(self):
        # Checks if the hash table has no elements
        for item in self.table:
            if item is not None: 
                return False
        return True
    
    def get_count(self):
        # Returns the total number of occupied slots in the table
        count = 0
        for item in self.table:
            if item is not None:
                count += 1
        return count
        
    def hash_function(self, key):
        # Calculates the index based on the key type (int or str)
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            total = 0
            for char in key:
                total += ord(char)
            return total % self.size
            
    def add(self, key, value):
        # Maps the key to an index and stores the (key, value) tuple
        index = self.hash_function(key)
        self.table[index] = (key, value)
                
    def get_by_key(self, key):
        # Retrieves the value associated with a specific key
        index = self.hash_function(key)
        if self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
        return None
                
    def get_by_value(self, value):
        # Search for a key by iterating through values (linear time)
        for i in range(self.size):
            if self.table[i] is not None and self.table[i][1] == value:
                return self.table[i][0]
        return None

# --- Testing the Hash Table ---
ht = HashTable(5)

# Adding keys
ht.add(1, "Value 1") 
ht.add(6, "Value 2") # Note: In this simple implementation, index 1 will be overwritten

# Output results
print(f"Value for key 1: {ht.get_by_key(1)}")
print(f"Value for key 6: {ht.get_by_key(6)}")
print(f"Total elements: {ht.get_count()}")