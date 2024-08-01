# Desafío: Juego de Preguntas y Respuestas
# Descripción:

# Vas a crear un juego de preguntas y respuestas donde se evaluarán las respuestas del usuario utilizando operadores lógicos. El juego constará de tres preguntas, y se evaluará si el usuario ha respondido correctamente a todas ellas.

# Requisitos:

# Inicializar Variables:

# Define las respuestas correctas para tres preguntas.
# Define las respuestas del usuario para cada pregunta.
# Evaluar Respuestas:

# Utiliza operadores lógicos para determinar si el usuario ha respondido correctamente a todas las preguntas.
# Mostrar Resultados:

# Imprime si el usuario ha ganado o perdido el juego basado en sus respuestas.
















# Inicializar Variables
respuesta_correcta_pregunta1 = "Python"
respuesta_correcta_pregunta2 = "Lista"
respuesta_correcta_pregunta3 = "Diccionario"

# Obtener Respuestas del Usuario
respuesta_usuario_pregunta1 = input("Pregunta 1: ¿Cuál es el lenguaje de programación que estás usando? ")
respuesta_usuario_pregunta2 = input("Pregunta 2: ¿Cómo se llama el tipo de colección ordenada en Python? ")
respuesta_usuario_pregunta3 = input("Pregunta 3: ¿Qué tipo de colección en Python utiliza pares clave-valor? ")

# Evaluar Respuestas usando Operadores Lógicos
# Verificar si todas las respuestas del usuario son correctas
respuesta_correcta_1 = respuesta_usuario_pregunta1 == respuesta_correcta_pregunta1
respuesta_correcta_2 = respuesta_usuario_pregunta2 == respuesta_correcta_pregunta2
respuesta_correcta_3 = respuesta_usuario_pregunta3 == respuesta_correcta_pregunta3

# Usar operadores lógicos para determinar si todas las respuestas son correctas
todas_correctas = respuesta_correcta_1 and respuesta_correcta_2 and respuesta_correcta_3

# Imprimir Resultados
print("\nResultado del Juego:")
print("Pregunta 1 correcta:", respuesta_correcta_1)
print("Pregunta 2 correcta:", respuesta_correcta_2)
print("Pregunta 3 correcta:", respuesta_correcta_3)
print("¿Todas las respuestas son correctas?:", todas_correctas)

