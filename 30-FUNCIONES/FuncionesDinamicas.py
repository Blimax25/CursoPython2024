#calcular el area de un cuadrado y un rectangulo
def calcular_area_forma(lado1,lado2=None):
    if lado2 is None:
        return lado1**2
    else:
        return lado1*lado2
    
print(calcular_area_forma(5))
print(calcular_area_forma(3,4))

#crear funcion que sume los numeros pares
def suma_pares_hasta(n):
    suma=0
    for i in range(2,n+1,2):
        suma += i
    return suma

print(suma_pares_hasta(10))

#Otros ejemplo
def suma_cudrados_cubos(n):
    suma_cuadrados = 0
    suma_cubos = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            suma_cuadrados += i**2
        else:
            suma_cubos +=i**3
    return suma_cuadrados, suma_cubos

cuadrados, cubos = suma_cudrados_cubos(5)
print("Suma de cuadrados: ", cuadrados)
print("Suma de cubos: ", cubos)
