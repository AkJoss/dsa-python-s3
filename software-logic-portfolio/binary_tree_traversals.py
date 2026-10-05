# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:30:43 2024

@author: José Alberto Rocha Munguía
"""

class Node:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, value):
        self.left = None   # Reference to the left child (homo)
        self.right = None  # Reference to the right child (hetero)
        self.data = value  # Value stored in the node
        
def inorder(root):
    """
    Performs In-order traversal: Left -> Root -> Right
    """
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    """
    Performs Pre-order traversal: Root -> Left -> Right
    """
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    """
    Performs Post-order traversal: Left -> Right -> Root
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Main execution block
if __name__ == "__main__":
    # Manual construction of the binary tree
    # root (groot) starts with value 12
    root = Node(12)
    
    # Left subtree construction
    root.left = Node(7)
    root.left.left = Node(4)
    root.left.left.left = Node(2)
    
    root.left.right = Node(9)
    root.left.right.left = Node(8)
    root.left.right.right = Node(11)
    
    # Right subtree construction
    root.right = Node(21)
    root.right.left = Node(16)
    root.right.left.right = Node(19)
    root.right.right = Node(25)
    
    # Display results
    print("In-order traversal:", end=" ")
    inorder(root)
    print("\nPre-order traversal:", end=" ")
    preorder(root)
    print("\nPost-order traversal:", end=" ")
    postorder(root)