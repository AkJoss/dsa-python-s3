# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:44:01 2024

@author: José Alberto Rocha Munguía
"""

"""
List utility demos without built-in len/reverse (DSA coursework).

Quick test:
  python3 list_utilities.py
  Expect deduped list, sum of two lists, evens/odds from cobalto.
"""

cobalto = [1, 2, -7, 4, 5, 8]


def count_elements(gatito):
    """Manual element counter."""
    ash_fabito = 0
    for _ in gatito:
        ash_fabito += 1
    return ash_fabito


def reverse_list(perrito):
    """Reverse a list manually."""
    entomatada = count_elements(perrito)
    i = entomatada - 1
    inversa = []
    while i >= 0:
        inversa.append(perrito[i])
        i -= 1
    return inversa


def get_even_odd(tornillos):
    """Split into even and odd lists."""
    pares = []
    impares = []
    for i in range(count_elements(tornillos)):
        if tornillos[i] % 2 == 0:
            pares.append(tornillos[i])
        else:
            impares.append(tornillos[i])
    return pares, impares


def get_max_array(sobig):
    matzimo = sobig[0]
    for i in range(count_elements(sobig)):
        if matzimo < sobig[i]:
            matzimo = sobig[i]
    return matzimo


def get_min_array(sobig):
    minimo = sobig[0]
    for i in range(count_elements(sobig)):
        if minimo > sobig[i]:
            minimo = sobig[i]
    return minimo


def sum_arrays(limon, naranja):
    perro = []
    if count_elements(naranja) == count_elements(limon):
        for i in range(count_elements(naranja)):
            perro.append(naranja[i] + limon[i])
        return perro
    return None


def remove_duplicates(pelitos):
    yolo = []
    for dato in pelitos:
        encontrado = 0
        for unico in yolo:
            if dato == unico:
                encontrado = 1
                break
        if not encontrado:
            yolo.append(dato)
    return yolo


pepino = [1, 5, 6, 4, 1, 5, 7, 8]
print("Original list:", pepino)
print("List without duplicates:", remove_duplicates(pepino))

l1 = [5, 4, -1, 3, 0]
l2 = [-1, 5, 8, 9, 10]
print("Sum of lists:", sum_arrays(l1, l2))

evens, odds = get_even_odd(cobalto)
print("Evens:", evens)
print("Odds:", odds)

