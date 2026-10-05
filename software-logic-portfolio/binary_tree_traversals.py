# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:30:43 2024

@author: José Alberto Rocha Munguía
"""

"""
Binary tree traversals demo (DSA coursework).

Builds a fixed tree and prints in-order, pre-order, and post-order walks.

Quick test:
  /opt/anaconda3/bin/python3 binary_tree_traversals.py
  Expect:
    In-order:  2 4 7 8 9 11 12 16 19 21 25
    Pre-order: 12 7 4 2 9 8 11 21 16 19 25
    Post-order: 2 4 8 11 9 7 19 16 25 21 12
"""


class Node:
    """One node in a binary tree (value + left/right children)."""

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def inorder(root):
    """In-order: Left -> Root -> Right."""
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    """Pre-order: Root -> Left -> Right."""
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    """Post-order: Left -> Right -> Root."""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


if __name__ == "__main__":
    root = Node(12)

    root.left = Node(7)
    root.left.left = Node(4)
    root.left.left.left = Node(2)

    root.left.right = Node(9)
    root.left.right.left = Node(8)
    root.left.right.right = Node(11)

    root.right = Node(21)
    root.right.left = Node(16)
    root.right.left.right = Node(19)
    root.right.right = Node(25)

    print("In-order traversal:", end=" ")
    inorder(root)
    print("\nPre-order traversal:", end=" ")
    preorder(root)
    print("\nPost-order traversal:", end=" ")
    postorder(root)
