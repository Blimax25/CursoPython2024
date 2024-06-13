"""
Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta 
función es devolver True 
si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True 
(6,0,5,1,0,3,0,1) >>> False
"""
import os           #Importar librería
os.system('cls')    #Limpiar pantalla

# Definición de la funicón
def dos_ceros(*args):
    i=0
    for item in args:
        if item==0:
            i+=1
    if i==2:
        print('True')
    else:
        print('False')

# Evaluación de la función 1
dos_ceros(5,6,1,0,0,9,3,5)
# Evaluación de la función 2
dos_ceros(6,0,5,1,0,3,0,1)
