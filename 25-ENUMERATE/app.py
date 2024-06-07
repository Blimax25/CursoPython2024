lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

print("\n")
#con enumarate
lista = ['a','b','c']
for i,item in enumerate(lista):
    print(i,item)
print("\n")

#Otro ejemplo range + enumerate
for i,item in enumerate(range(50,55)):
    print(i,item)
print("\n")

#crear lista de tuplas
lista = ['a','b','c']
mis_tuplas=list(enumerate(lista))
print(mis_tuplas)
print(mis_tuplas[1][0])