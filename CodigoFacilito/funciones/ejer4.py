"""
Define una función que permita conocer si el primer y último elemento de una lista son el mismo elemento. 
La función debe tener por nombre “iguales”. 
La función debe recibir como argumento una lista de números enteros con longitud mayor a 2. 
La función debe retornar verdadero o falso si el primer y último elemento son el mismo número.

- Si la función recibe una lista con 2 o menos elementos retornará None.  
"""

def iguales(unaLista):
    if(len(unaLista) <= 2):
        return None
    if unaLista[0] == unaLista[-1]:
        return True
    else:
        return False
    
        