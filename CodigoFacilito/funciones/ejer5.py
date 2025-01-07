"""
Define una función que nos permita conocer si todos los elementos de una lista son el mismo. 
La función debe tener por nombre “iguales” y debe recibir como argumento un listado de números enteros.
La función debe retornar True o False si todos los elementos de la lista son el mimos.

- La función retornará None si la lista se encuentra vacía o solo posee un elemento.
"""

def condicion(unaFuncion):
    def nueva_funcion(unaLista):
        if len(unaLista) <= 1:
            return None
        else: return unaFuncion(unaLista)
    return nueva_funcion


@condicion
def iguales(unaLista):
    aux = unaLista[0]
    for elemento in unaLista:
        if elemento != aux:
            return False
    return True

# Pruebas de la función
print(iguales([1, 1, 1])) # Debe retornar True 
print(iguales([1, 2, 1])) # Debe retornar False 
print(iguales([])) # Debe retornar None 
print(iguales([1])) # Debe retornar None