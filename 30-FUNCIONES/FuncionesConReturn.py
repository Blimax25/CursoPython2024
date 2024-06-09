#verificar si un numero es par
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
#llamar a la función
print(es_par(3))
print(es_par(6))

#calcular factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1) #recursividad: se llama a sí mismo
#llamada a función
print(factorial(5))