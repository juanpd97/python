"""
Usando la siguiente lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] genera una tupla llamada pares. Imprime dicha tupla en consola.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = tuple(num for num in lista if num % 2 == 0)

print(pares)

