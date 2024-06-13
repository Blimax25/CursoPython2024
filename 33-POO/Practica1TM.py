"""
Práctica Tipos de Métodos 1
Crea un método estático respirar() para la clase Mascota. 
Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
"""
class Mascota:
    #metodo estatico
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

#crear objeto
Mascota.respirar()