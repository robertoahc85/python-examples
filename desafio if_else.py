# #Objetivo: Crear un programa que permita al usuario adivinar un número secreto. 
# El programa debe dar una sola oportunidad al usuario para adivinar 
# y debe indicar si el usuario adivinó correctamente o no.

# Instrucciones:

# Genera un número secreto.
# Pide al usuario que adivine el número.
# Usa estructuras if y else para comparar la adivinanza del usuario con el número secreto.
# Indica al usuario si su adivinanza es correcta o no.



















import random

# Generar un número secreto
numero_secreto = random.randint(1, 10)

# Pedir al usuario que adivine el número
print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número entre 1 y 10.")
adivinanza = int(input("Introduce tu adivinanza: "))

# Comparar la adivinanza del usuario con el número secreto
if adivinanza < numero_secreto:
    print("Tu adivinanza es demasiado baja.")
elif adivinanza > numero_secreto:
    print("Tu adivinanza es demasiado alta.")
else:
    print("¡Felicidades! Adivinaste el número.")

print("Gracias por jugar. ¡Hasta la próxima!")
