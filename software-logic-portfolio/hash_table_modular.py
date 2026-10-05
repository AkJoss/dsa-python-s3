# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:35:53 2024

@author: José Alberto Rocha Munguía
"""

"""
Hash table demo (modular / collision overwrite) — DSA coursework.

Same collision idea as hash_table.py; prints "Total rateros" (occupied slots).

Quick test:
  python3 hash_table_modular.py
  Expect Key 1: None, Key 6: value2, Total rateros: 1
"""


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def is_empty(self):
        for i in range(self.size):
            if self.table[i] is not None:
                return False
        return True

    def get_ratero_count(self):
        count = 0
        for i in range(self.size):
            if self.table[i] is not None:
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


hash_table = HashTable(5)
hash_table.add(1, "value1")
hash_table.add(6, "value2")

print(f"Key 1: {hash_table.get_by_key(1)}")
print(f"Key 6: {hash_table.get_by_key(6)}")
print(f"Total rateros: {hash_table.get_ratero_count()}")

