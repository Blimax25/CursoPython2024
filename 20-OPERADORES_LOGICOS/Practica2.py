"""
Practica 2.

Verifica si las palabras almacenadas en las siguientes variables:

palabra1 = "éxito", y
palabra2 = "tecnología"

no se encuentran en la frase a continuación, y almacena 
el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:

"Cuando algo es lo suficientemente importante, lo haces incluso 
si las probabilidades de que salga bien no te acompañan"

Elon Musk
"""

palabra1 = "éxito"
palabra2 = "tecnología"

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"

mi_bool = (not(palabra1 in frase)) and (not(palabra2 in frase))
print(mi_bool)
