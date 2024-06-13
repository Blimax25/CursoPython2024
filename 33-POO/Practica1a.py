"""

Práctica Atributos 1
Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.

Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad
de pisos igual a 4.
"""
class Casa:                                         #clase
    def __init__(self,color,cantidad_pisos):        #constructor
            self.color = color                      #atributo
            self.cantidad_pisos = cantidad_pisos    #atributo

#creacion de objetos
casa_blanca = Casa('blanco', '4')
#verificación
print(f'casa de color {casa_blanca.color} y de {casa_blanca.cantidad_pisos} pisos')
