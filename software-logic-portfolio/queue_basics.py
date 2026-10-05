# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:55:48 2024

@author: José Alberto Rocha Munguía
"""

class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0
        
    def enqueue(self, item):
        # Add an element to the rear of the queue
        self.items.append(item)
            
    def dequeue(self):
        # Remove the front element
        if self.is_empty():
            raise IndexError("The queue is empty; cannot dequeue.")
        return self.items.pop(0)
        
    def size(self):
        # Get the size of the queue
        return len(self.items)
        
    def peek(self):
        # Look at the front element without removing it
        if self.is_empty():
            raise IndexError("The queue is empty; cannot peek.")
        return self.items[0]

# --- Testing the Queue ---
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