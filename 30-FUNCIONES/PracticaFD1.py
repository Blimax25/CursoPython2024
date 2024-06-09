"""
Practica 1
Crea una función (todos_positivos) que reciba una lista de números 
como parámetro, y devuelva True si todos los valores de una lista 
son positivos, y False si al menos uno de los valores es negativo. 
Crea una lista llamada lista_numeros con valores positivos y negativos.
"""

def todos_positivos(lista):
    positivos=True
    for i in range(1,len(lista)):
        if lista[i]<0: #verificación si es negativo
            positivos = positivos and False
        else:          #verificación si es positivo
            positivos = positivos and True
    return positivos


lista_numeros = [1,-50,502,-5000,755,600,33,61]
print(todos_positivos(lista_numeros))
lista_numeros = [1,50,502,5000,755,600,33,61]
print(todos_positivos(lista_numeros))