"""
Practica 3
Declara una función llamada cuadrado, que tome como argumento 
un número cualquiera, y que cada vez que sea llamada, imprima 
en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).

El nombre del argumento que debe tomar dicha función es un_numero. 
Crea dicha variable y asígnale un número cualquiera.
"""
def cuadrado(un_numero):
    print(f"{un_numero}^2 = {un_numero**2}")

num = 4
cuadrado(num)