# Desafío: Evaluación de Información Personal
# Descripción:

# Vas a crear un programa que obtiene información personal de tres personas desde la consola 
# y realiza algunos cálculos utilizando esta información. El programa debe:

# Obtener los nombres, edades y alturas de tres personas desde la consola.
# Calcular el promedio de las edades y alturas(flotante).
# Calcular el total de caracteres en los nombres.
# Imprimir los resultados.
# Requisitos:

# Obtener Datos de Consola:

# Usa la función input() para obtener el nombre, edad y altura de tres personas.
# Calcular Promedios y Totales:

# Calcula el promedio de las edades.
# Calcula el promedio de las alturas.
# Calcula el total de caracteres en los nombres.
# Mostrar Resultados:

# Imprime el promedio de las edades y alturas.
# Imprime el total de caracteres en los nombres.









# Obtener Datos de Consola para Persona 1
nombre_persona1 = input("Ingrese el nombre de la Persona 1: ")
edad_persona1 = int(input("Ingrese la edad de la Persona 1: "))
altura_persona1 = float(input("Ingrese la altura de la Persona 1 en metros: "))

# Obtener Datos de Consola para Persona 2
nombre_persona2 = input("Ingrese el nombre de la Persona 2: ")
edad_persona2 = int(input("Ingrese la edad de la Persona 2: "))
altura_persona2 = float(input("Ingrese la altura de la Persona 2 en metros: "))

# Obtener Datos de Consola para Persona 3
nombre_persona3 = input("Ingrese el nombre de la Persona 3: ")
edad_persona3 = int(input("Ingrese la edad de la Persona 3: "))
altura_persona3 = float(input("Ingrese la altura de la Persona 3 en metros: "))

# Calcular Promedios
promedio_edad = (edad_persona1 + edad_persona2 + edad_persona3) / 3
promedio_altura = (altura_persona1 + altura_persona2 + altura_persona3) / 3

# Calcular Total de Caracteres en Nombres
total_caracteres_nombres = len(nombre_persona1) + len(nombre_persona2) + len(nombre_persona3)

# Imprimir Resultados
print("\nResultados:")
print("Promedio de Edades:", promedio_edad)
print("Promedio de Alturas:", promedio_altura)
print("Total de Caracteres en Nombres:", total_caracteres_nombres)
