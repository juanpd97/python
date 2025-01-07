"""
Define un función llamada “promedio” que permita calculas el promedio de una lista.
 La función debe recibir como argumento una lista de números enteros y retornar el promedio de dicha lista.
"""

def promedio(unaLista):
    suma = 0
    for numero in unaLista:
        suma += numero
    return suma/len(unaLista)
