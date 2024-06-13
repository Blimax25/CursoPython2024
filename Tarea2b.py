"""
Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro, y 
que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
Por ejemplo si al invocar esta función pasamos la palabra "entretenido", debería devolver ['d', 'e', 'ï', 'n', 'o', 'r', 't']
"""
import os           #Importar librería
os.system('cls')    #Limpiar pantalla

# Definición de la funicón
def letras_unicas(palabra):
    resultado = []
    for letra in palabra:
        if letra not in resultado:
            resultado.append(letra)
    resultado.sort()
    print(resultado)

# Evaluación de la función 1
palabra1 = 'entretenido'
letras_unicas(palabra1)
# Evaluación de la función 2
palabra1 = 'hipopotamo'
letras_unicas(palabra1)