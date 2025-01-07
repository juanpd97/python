"""
Define una función que permita conocer cuantas vocales posee un string. 
La función debe tener por nombre “vocales” y debe recibir como argumento un string. 
La función debe retornar la cantidad de vocales que dicho string posee.
"""

def vocales(unString):
    contador = 0
    for vocal in unString.lower():
        if vocal in 'aeiou':
            contador += 1

    return contador

print(vocales('BUen Dia'))