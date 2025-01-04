"""
Utilizando el diccionario del paso anterior (my_dictionary):
Reemplaza el valor de edad por 20 y 
añade una nueva llave llamada: ‘active’ que almacenara un valor bool (True o False). 
Reemplaza la llave course por courses(Plural) Imprime el diccionario en consola.

Nota: Estos pasos debe hacerse utilizando los métodos del objeto diccionario.
"""

my_dictionary = {'name':  'Cody', 'age': 12, 'course': 'python'}


my_dictionary.pop('course')

my_dictionary.update({
    'age': 20,
    'active': True,
    'courses': 'python'  
})

print(my_dictionary)