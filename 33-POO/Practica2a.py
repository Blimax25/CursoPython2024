"""
Práctica Atributos 3
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:
real = False

Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
especie = "Humano"
magico = True
edad = 17
"""
class Personaje:                                 #clase
    real = False

    def __init__(self,especie,magico,edad):      #constructor
            self.especie = especie               #atributo
            self.magico = magico                 #atributo
            self.edad = edad                     #atributo

#creacion de objetos
harry_potter = Personaje('Humano', real, '17')
#verificación
print(f'Harry Potter: {harry_potter.especie} de {harry_potter.edad} años 
      con estado mágico {harry_potter.magico}')
