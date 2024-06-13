class Pajaro:
    def __init__(self,color,especie): #constructor
        self.color = color
        self.especie = especie

#creacion de objetos
mi_pajaro = Pajaro('negro', 'Tucan')

print(f'mi_pajaro es un {mi_pajaro.especie} y de color {mi_pajaro.color}')