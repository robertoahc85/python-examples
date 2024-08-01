x = 10
if x > 5:
    print("x es mayor que 5")


x = 3

if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5")

x = 7

if x > 10:
    print("x es mayor que 10")
elif x > 5:
    print("x es mayor que 5 pero menor o igual a 10")
else:
    print("x es 5 o menor")



x = 15

if x < 10:
    print("x es menor que 10")
elif x == 10:
    print("x es igual a 10")
elif x < 20:
    print("x es mayor que 10 pero menor que 20")
else:
    print("x es 20 o mayor")



# Supongamos que estamos creando un formulario de registro y necesitamos validar la edad del usuario.


edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Debes tener al menos 18 años para registrarte.")
elif 18 <= edad <= 120:
    print("Registro exitoso. Bienvenido!")
else:
    print("Edad no válida. Por favor, ingresa una edad correcta.")
    
    
#  Un sistema que asigna una calificación basada en el puntaje del estudiante.

puntaje = int(input("Ingrese el puntaje del examen: "))

if puntaje >= 90:
    calificacion = 'A'
elif puntaje >= 80:
    calificacion = 'B'
elif puntaje >= 70:
    calificacion = 'C'
elif puntaje >= 60:
    calificacion = 'D'
else:
    calificacion = 'F'

print(f"La calificación del estudiante es: {calificacion}")


# "Un programa que calcula la tarifa de envío basada en el peso del paquete.

peso = float(input("Ingrese el peso del paquete en kg: "))

if peso <= 1:
    tarifa = 5.00
elif peso <= 5:
    tarifa = 10.00
elif peso <= 10:
    tarifa = 20.00
else:
    tarifa = 30.00

# print(f"La tarifa de envío es: ${tarifa:.2f}")"