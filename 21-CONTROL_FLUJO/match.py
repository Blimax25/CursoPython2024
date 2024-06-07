#comparación de números
number = 6
match number:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 1:
        print("Tres")
    case _:
        print("Otro número")
    
#comparación de tipos
value = "Hola"
match value:
    case int():
        print("Es un entero")
    case str():
        print("Es una cadena")
    case list():
        print("Es una lista")
    case _:
        print("Tipo desconocido")
