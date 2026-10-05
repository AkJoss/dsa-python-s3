"""
Sorting Benchmark (DSA coursework).

@author José Alberto Rocha Munguía
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:17:02 2024

@author: josea
"""
import random
import time
from bubble_sort import Bubble_Sort
from insertion_sort import Insertion_Sort

#ejemplo de uso
#arr = [5,3,8,4,2]
arr = [random.randint(1,50) for i in range(50000)]
print(f"Ordenar {len(arr)} numeros lleva:\n")
###########################################
############ BUBBLE SORT ##################
###########################################

#medir el tiempo de ejecución
start_time = time.time()
print(Bubble_Sort(arr))
#Termine de ordenar el arreglo
end_time = time.time()
#mostrar el tiempo de ejecución
print("Tiempo de ejecucion: {:.6f} segundos".format(end_time - start_time))

###########################################
############ INSERTION SORT ###############
###########################################
#medir el tiempo de ejecución
start_time = time.time()
print(Insertion_Sort(arr))
#Termine de ordenar el arreglo
end_time = time.time()
#mostrar el tiempo de ejecución
print("Tiempo de ejecucion: {:.6f} segundos".format(end_time - start_time))