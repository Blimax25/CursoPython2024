"""
Práctica Abrir y Manipular Archivos 3
Abre el archivo texto.txt e imprime únicamente la segunda línea.
"""
#Abrir archivo
mi_archivo = open('prueba.txt')

#Leer primera línea
for i in range(1,3,1):
    seglinea = mi_archivo.readline()
print(seglinea)
#Cerrar archivo
mi_archivo.close()