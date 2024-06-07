"""
Descripción:
Crea un programa que pida al usuario dos números y una operación (suma, resta, multiplicación, división).
Utiliza match-case para realizar la operación correspondiente y muestra el resultado.
"""
num1 = input("Ingrese el número1: ")
num1f = float(num1)
num2 = input("Ingrese el número2: ")
num2f = float(num2)
oper = input("Ingrese la operación a realizar (suma, resta, multiplicacion, division): ")
match oper:
    case "suma":
        result = num1f + num2f
    case "resta":
        result = num1f - num2f
    case "multiplicacion":
        result = num1f * num2f
    case "division":
        result = num1f / num2f
    case _:
        result = "Digitar la operación de forma textual a las opciones presentadas."
print(f"resultado: {result}")