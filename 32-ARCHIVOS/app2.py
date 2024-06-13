archivo = open('prueba2.txt', 'w') # Si no existe el archivo, se crea el mismo
archivo.write('hola\n')
archivo.write('mundo')
#modificar archivo
archivo = ('prueba2.txt','m')

lista = ['hola', 'mund0', 'aqui', 'estoy']

for p in lista:
    archivo.writelines()

archivo.close()