# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:55:48 2024

@author: José Alberto Rocha Munguía
"""

"""
Queue basics demo (DSA coursework).

Quick test:
  python3 queue_basics.py
  Expect empty->False after enqueue, size changes, front Le Grute then Scarlett.
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty; cannot dequeue.")
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            raise IndexError("The queue is empty; cannot peek.")
        return self.items[0]


q = Queue()
print(f"Is queue empty? {q.is_empty()}")

q.enqueue("Le Grute")
print(f"Is queue empty? {q.is_empty()}")
print(f"Queue size: {q.size()}")
print(f"Front element: {q.peek()}")

q.enqueue("Scarlett Johansson")
print(f"Queue size: {q.size()}")

q.dequeue()
print(f"Queue size after dequeue: {q.size()}")
print(f"New front element: {q.peek()}")

