"""
Practica 1
Utilizando las variables num1 y num2, que se alimentan con el 
input del usuario (tal como en el código ya proporcionado):

Crea una estructura de control de flujo que compare los 
valores de las variables, y arroje un resultado de acuerdo al caso:

"num1 es mayor que num2"
"num2 es mayor que num1"
"num1 y num2 son iguales"

Debes mostrar en pantalla el valor de las variables ingresadas en 
lugar de num1 y num2.

Aclaración:
1. No deben imprimirse strings adicionales a la respuesta del usuario.
2. Los ejercicios que contienen el la función input() deben ser probados con el botón: "Ejecutar pruebas". Ya que el botón "Ecutar código" arrojará el siguiente error: "EOF when reading a line".
"""
num1 = input("Ingrese el número1: ")
num2 = input("Ingrese el número2: ")

if (num1>num2):
    print(num1,' es mayor que ',num2)
elif (num2>num1):
    print(num2,' es mayor que ',num1)
else:
    print(num1, "es igual a ", num2)
