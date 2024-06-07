#ejemplo 1
lista = ['a','b','c','d']
for item in lista:
  numero_letra = lista.index(item) + 1
  print(f"letra {numero_letra}: {item}")

#ejemplo2
lista = ['pablo', 'laura', 'jose', 'luis', 'julia']
for item in lista:
  if item.startswith('l'):
    print(item)
  else:
    print("Nombre que no comienze con L")
#ejemplo3
#directamente
for a,b in [[11,2],[2,3],[5,6]]:
  print(f"{a} - {b}")
#ejemplo4
