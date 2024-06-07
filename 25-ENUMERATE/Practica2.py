"""
Practica 2

Crea una lista formada por las tuplas (indice, elemento), 
formadas a partir de obtener mediante enumerate() los índices 
de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices .
"""
frase = "Python"
lista_indices = list(enumerate(frase))
print(lista_indices)
