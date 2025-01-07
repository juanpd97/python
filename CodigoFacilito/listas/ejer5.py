"""
Crea una matriz de 3x3 e imprime en consola True si: El primer elemento de cada fila es un número par. 
El nombre de la matriz debe ser matrix.
"""

matrix = [
    [0 ,1 ,2],
    [3 ,4 ,5],
    [6 ,7 ,8]
]

print( (matrix[0][0]%2 == 0) and (matrix[1][0]%2 == 0) and (matrix[2][0]%2 == 0))