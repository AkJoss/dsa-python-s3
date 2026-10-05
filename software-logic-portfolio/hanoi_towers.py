# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:49:02 2024

@author: José Alberto Rocha Munguía
"""

"""
Towers of Hanoi recursive solver (DSA coursework).

Quick test:
  python3 hanoi_towers.py
  Expect move steps for 5 disks from A to B using C (31 lines of moves).
"""


def hanoi(origin, destination, auxiliary, n):
    """Solve Towers of Hanoi; print each disk move."""
    if n == 1:
        print(f"Move disk 1 from tower {origin} to tower {destination}")
        return

    hanoi(origin, auxiliary, destination, n - 1)
    print(f"Move disk {n} from tower {origin} to {destination}")
    hanoi(auxiliary, destination, origin, n - 1)


n_disks = 5
hanoi("A", "B", "C", n_disks)

