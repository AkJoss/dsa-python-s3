# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:49:02 2024

@author: José Alberto Rocha Munguía
"""

def hanoi(origin, destination, auxiliary, n):
    """
    Solves the Towers of Hanoi puzzle using recursion.
    a: origin
    b: destination
    c: auxiliary
    """
    # Base case: If there is only one disk, move it directly from origin to destination
    if n == 1:
        print(f"Move disk 1 from tower {origin} to tower {destination}")
        return None

    # Step 1: Move n-1 disks from origin to auxiliary using destination as support
    hanoi(origin, auxiliary, destination, n - 1)
    
    # Step 2: Move the nth disk from origin to destination
    print(f"Move disk {n} from tower {origin} to {destination}")
    
    # Step 3: Move the n-1 disks from auxiliary to destination using origin as support
    hanoi(auxiliary, destination, origin, n - 1)

# --- Usage Example ---
n_disks = 5
hanoi("A", "B", "C", n_disks)