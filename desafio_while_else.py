
# Desafío: Piedra, Papel o Tijera
# Crea un juego de "Piedra, Papel o Tijera" en Python que cumpla con los siguientes requisitos:

# El programa debe solicitar al usuario que ingrese su elección (piedra, papel o tijera).
# El programa debe generar aleatoriamente una elección para la computadora.
# El programa debe determinar el ganador según las reglas clásicas del juego:
# Piedra aplasta Tijera.
# Tijera corta Papel.
# Papel envuelve Piedra.
# El programa debe preguntar al usuario si quiere jugar otra vez después de cada ronda.
# Si el usuario responde "no", el bucle debe terminar y el programa debe mostrar un mensaje de despedida.
# Utiliza un bucle while junto con else para implementar el juego.



import random

# Función para obtener la elección de la computadora
def obtener_eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

# Función para determinar el ganador
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "tijera" and computadora == "papel") or \
         (usuario == "papel" and computadora == "piedra"):
        return "¡Ganaste!"
    else:
        return "Perdiste..."

# Bucle principal del juego
while True:
    usuario = input("Elige piedra, papel o tijera: ").lower()
    
    if usuario not in ["piedra", "papel", "tijera"]:
        print("Elección inválida. Intenta de nuevo.")
        continue
    
    computadora = obtener_eleccion_computadora()
    print(f"La computadora eligió: {computadora}")
    
    resultado = determinar_ganador(usuario, computadora)
    print(resultado)
    
    jugar_otra_vez = input("¿Quieres jugar otra vez? (sí/no): ").lower()
    if jugar_otra_vez != "sí":
        break
else:
    print("Gracias por jugar. ¡Hasta luego!")

print("Juego terminado.")
