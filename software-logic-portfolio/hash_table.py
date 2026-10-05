# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:16:29 2024

@author: José Alberto Rocha Munguía
"""

"""
Simple hash table demo without collision chaining (DSA coursework).

Keys 1 and 6 both map to index 1 (size 5), so the second add overwrites.

Quick test:
  python3 hash_table.py
  Expect key 1 -> None (overwritten), key 6 -> Value 2, Total elements: 1
"""


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def is_empty(self):
        for item in self.table:
            if item is not None:
                return False
        return True

    def get_count(self):
        count = 0
        for item in self.table:
            if item is not None:
                count += 1
        return count

    def hash_function(self, key):
        if isinstance(key, int):
            return key % self.size
        if isinstance(key, str):
            total = 0
            for char in key:
                total += ord(char)
            return total % self.size
        return None

    def add(self, key, value):
        index = self.hash_function(key)
        self.table[index] = (key, value)

    def get_by_key(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None and self.table[index][0] == key:
            return self.table[index][1]
        return None

    def get_by_value(self, value):
        for i in range(self.size):
            if self.table[i] is not None and self.table[i][1] == value:
                return self.table[i][0]
        return None


ht = HashTable(5)
ht.add(1, "Value 1")
ht.add(6, "Value 2")  # collision: overwrites index 1

print(f"Value for key 1: {ht.get_by_key(1)}")
print(f"Value for key 6: {ht.get_by_key(6)}")
print(f"Total elements: {ht.get_count()}")

