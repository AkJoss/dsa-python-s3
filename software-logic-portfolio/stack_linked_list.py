# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:39:27 2024

@author: José Alberto Rocha Munguía
"""

"""
Stack implemented with a linked list (DSA coursework).

Quick test:
  python3 stack_linked_list.py
  Expect push/pop/display lines ending with Nicolas Maduro on top.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        print(f"Adding {data} to the top of the stack")
        if self.top is None:
            self.top = Node(data)
            return

        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("There are no elements in the stack to pop")
            return
        print(f"Popping {self.top.data}")
        self.top = self.top.next

    def display(self):
        print("Displaying the stack")
        temp_node = self.top
        while temp_node is not None:
            print(f"{temp_node.data}", end=", ")
            temp_node = temp_node.next
        print("")


stack = Stack()
stack.push("Leon S. Kennedy")
stack.push("SpongeBob")
stack.push("Henry Cavill")
stack.display()

stack.pop()
stack.display()

stack.pop()
stack.display()

stack.push("Nicolas Maduro")
stack.display()

