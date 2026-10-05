# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:44:01 2024

@author: José Alberto Rocha Munguía
"""
cobalto = [1, 2, -7, 4, 5, 8]

def count_elements(gatito):  
    """Manual element counter."""
    ash_fabito = 0 # This is a counter
    for datito in gatito:
        ash_fabito += 1
    return ash_fabito

def reverse_list(perrito):
    """Reverses the list using your 'entomatada' logic."""
    entomatada = count_elements(perrito)
    i = entomatada - 1
    inversa = []
    while i >= 0:
        inversa.append(perrito[i])
        i -= 1
    return inversa

def get_even_odd(tornillos):
    """Separates numbers into even and odd lists."""
    pares = []
    impares = []
    for i in range(count_elements(tornillos)):
        if tornillos[i] % 2 == 0:
           pares.append(tornillos[i])
        else:
           impares.append(tornillos[i])
    return pares, impares

def get_max_array(sobig):
    """Finds the maximum value in the array."""
    matzimo = sobig[0]
    for i in range(count_elements(sobig)):
        if matzimo < sobig[i]:
            matzimo = sobig[i]
    return matzimo
    
def get_min_array(sobig):
    """Finds the minimum value in the array."""
    minimo = sobig[0]
    for i in range(count_elements(sobig)):
        if minimo > sobig[i]:
            minimo = sobig[i]
    return minimo

def sum_arrays(limon, naranja):
    """Sums two arrays element by element."""
    perro = []
    if count_elements(naranja) == count_elements(limon):
        for i in range(count_elements(naranja)):
            perro.append(naranja[i] + limon[i])
        return perro

def remove_duplicates(pelitos):
    """Removes duplicate values from the list using 'yolo' logic."""
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

# --- Test Execution ---
pepino = [1, 5, 6, 4, 1, 5, 7, 8]
print("Original list:", pepino)
print("List without duplicates:", remove_duplicates(pepino))

l1 = [5, 4, -1, 3, 0]
l2 = [-1, 5, 8, 9, 10]
print("Sum of lists:", sum_arrays(l1, l2))

evens, odds = get_even_odd(cobalto)
print("Evens:", evens)
print("Odds:", odds)