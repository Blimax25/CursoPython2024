#forma tradicional
palabra = 'python'
lista = []

for item in palabra:
    lista.append(item)
#print(lista)

#comprension lista
lista = [item for item in 'python']
#print(lista)

#sintaxis
#nueva_lista=[expresion for item in iterable if condicion==True]
lista = [item/2 for item in range(0,21,2)]
print(lista)