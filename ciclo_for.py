# for elemento in secuencia:
#     # Hacer algo con el elemento

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

palabra = "Python"
for letra in palabra:
   print(letra.upper())
    
#  Uso de enumerate() para obtener índice y valor: 
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"Índice {indice}: {color}")
    
# Uso de zip() para iterar sobre múltiples listas simultáneamente:   
nombres = ["Ana", "Carlos", "Eva"]
edades = [25, 30, 28]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# Uso de break para salir del bucle:
for numero in range(10):
    if numero == 5:
        break
    print(numero)
#  Uso de continue para saltar una iteración   
for numero in range(10):
    if numero % 2 == 0:
        continue
    print(numero)   
    

# Puedes usar la función range() para generar una secuencia de números:
for i in range(5):
    print(i)


#ejemplo en diccionario
estudiantes = {"Ana": 10, "Luis": 9, "Carlos": 8}
for nombre in estudiantes:
    print(nombre)  
    



for nombre, nota in estudiantes.items():
    print(f"{nombre} tiene una nota de {nota}")
    

# Calcular la media de una lista de números.
numeros = [23, 76, 34, 89, 12, 67, 54]
suma = 0

for numero in numeros:
    suma += numero

media = suma / len(numeros)
print(f"La media de los números es {media}")

# Sumar los valores de un diccionario.

ventas = {"enero": 1000, "febrero": 1500, "marzo": 1200}
total_ventas = 0

for mes, cantidad in ventas.items():
    total_ventas += cantidad

print(f"El total de ventas es {total_ventas}")


# Filtrar una lista de números para obtener solo los pares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Números pares: {pares}")



