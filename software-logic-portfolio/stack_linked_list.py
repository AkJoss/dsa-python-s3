# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:39:27 2024

@author: José Alberto Rocha Munguía
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
        # If there is no data, add the element as the top element
        if self.top == None:
            self.top = Node(data)
            return 0 
        
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        # If there is no data in the top node, we return
        if self.top == None:
            print("There are no elements in the stack to pop")
            return 0
        print(f"Popping {self.top.data}")
        self.top = self.top.next 
    
    def display(self):
        print("Displaying the stack")
        # Traverse the stack and print values
        temp_node = self.top 
        while temp_node != None:
            print(f"{temp_node.data}", end=", ")
            temp_node = temp_node.next 
        print("")

# --- Stack Usage ---
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