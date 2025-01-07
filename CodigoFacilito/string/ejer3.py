"""
Crea una variable de tipo string llamada name e imprime en consola True o False si el primer o último carácter
 son vocales.
"""

name = 'juanpA'
aux = 'aeiou'
name = name.lower()

print(name[0] in aux or name[-1] in aux) 
