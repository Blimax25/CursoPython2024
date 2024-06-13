"""
Práctica Métodos 3
Crea una instancia de la clase Alarma, que tenga un método 
llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"
"""
class Alarma:

    def postergar(self, cantidad_minutos): #constructor de metodo
        print(f'La alarma ha sido pospuesta {cantidad_minutos} minutos')
    
#creacion de objetos
alarm1= Alarma()
#llamada a métodos piar y volar
alarm1.postergar(10)