"""
Crea una función llamada devolver_distintos que reciba 3 integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio.
"""
import os           #Importar librería
os.system('cls')    #Limpiar pantalla

# Definición de la funicón
def devolver_distintos(a, b, c):
    suma = a+b+c
    mayor = max(a,b,c)
    menor = min(a,b,c)
    medio = a
    for i in list([a,b,c]):
        if (i!=mayor)and(i!=menor):
            medio = i
    if suma>15:
        return print(f'El número mayor es: {mayor}')
    elif suma<10:
        return print(f'El número menor es: {menor}')
    else:
        return print(f'El número intermedio es: {medio}')

# Evaluación de la función 1
num1 = 1
num2 = 5
num3 = 4
devolver_distintos(num1, num2, num3)
# Evaluación de la función 2
num1 = 10
num2 = 5
num3 = 4
devolver_distintos(num1, num2, num3)
# Evaluación de la función 3
num1 = 1
num2 = 2
num3 = 4
devolver_distintos(num1, num2, num3)