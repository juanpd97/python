"""
Crea una lista de longitud 5 que contengan tuplas de 2 elementos de números enteros.
(e.g (10, 20) ) . Utilizando un ciclo for-each, imprime en consola las tuplas.
Cada impresión en consola (Una por cada elemento)
debe seguir el siguiente formato: ‘{first_element} - {second_element}’. 
La lista debe tener por nombre: my_list
E.g
my_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

>>> 1 - 2
>>> 3 - 4
>>> 5 - 6
>>> 7 - 8
>>> 9 - 10
"""

my_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

for x,y in my_list:
    print(f'{x}  - {y}')