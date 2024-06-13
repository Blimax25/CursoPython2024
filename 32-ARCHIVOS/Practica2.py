"""
Práctica Abrir y Manipular Archivos 2
Imprime la primera línea del archivo texto.txt
No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.
"""
#Abrir archivo
mi_archivo = open('prueba.txt')

#Leer primera línea
print(mi_archivo.readline())
#Cerrar archivo
mi_archivo.close()