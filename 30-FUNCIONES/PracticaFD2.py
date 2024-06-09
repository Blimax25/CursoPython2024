lista_numeros = [1,50,500,5000,750,600]
def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0:
            suma += n
            print(suma)
        elif n < 1000:
            #suma += n
            print(suma)
        else:
            pass
    return suma

print(suma_menores(lista_numeros))