"""
Define una lista de longitud 10 de Strings. 
La lista debe tener por nombre strings_list Genera una sub lista con los 3 primeros y últimos elementos.
Imprime en consola la nueva sub lista.
"""

strings_list = ["cadena1", "cadena2", "cadena3", "cadena4", "cadena5", "cadena6", "cadena7", "cadena8", "cadena9", "cadena10"]
sub_lista = strings_list[:3]
sub_lista.extend(strings_list[-3:])
print(sub_lista)
