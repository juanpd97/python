#Utilizando el diccionario del paso anterior (my_dictionary): Genera un nuevo string con las llaves del diccionario. Las llaves debe encontrarse separadas por un guión (-). Imprime dicho string en consola.
my_dictionary = {'name':  'Cody', 'age': 12, 'course': 'python'}

aux = '-'.join(my_dictionary.keys())

print(aux)
