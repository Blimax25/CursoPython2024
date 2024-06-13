class Pajaro:
    def __init__(self,color,especie): #metodo constructor
        self.color = color
        self.especie = especie
    
    def piar(self):
        print('Pio')

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")
    
#creacion de objetos
piolin = Pajaro('amarillo','canario')
print(piolin.especie)
#llamada a métodos piar y volar
piolin.piar()
piolin.volar(3)