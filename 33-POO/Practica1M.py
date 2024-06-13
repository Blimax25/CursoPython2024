"""
Práctica Métodos 1
Crea una clase Perro. Dicho perro debe poder ladrar.

Crea el método ladrar() y ejecútalo en una instancia de Perro. 
Cada vez que ladre, debe mostrarse en pantalla "Guau!".
"""
class Perro:

    def ladrar(self):
        print('Guau!')
    
#creacion de objetos
beto = Perro()
#llamada a métodos piar y volar
beto.ladrar()
