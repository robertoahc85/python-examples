# Ejemplo de uso de for-else para buscar un número en una lista
numeros = [1, 2, 3, 4, 5]
buscar = 7

for numero in numeros:
    if numero == buscar:
        print(f"Número {buscar} encontrado.")
        break
else:
    print(f"Número {buscar} no encontrado.")
    
 #Imaginemos que queremos buscar un nombre específico en una lista de nombres:

nombres = ["Ana", "Pedro", "Maria", "Luis"]
buscar = "Carlos"

for nombre in nombres:
    if nombre == buscar:
        print(f"Nombre {buscar} encontrado.")
        break
else:
    print(f"Nombre {buscar} no encontrado.")
    
#  Verificar si todas las contraseñas en una lista cumplen con un criterio específico (por ejemplo, longitud mínima de 8 caracteres):

contraseñas = ["abc12345", "contraseñaSegura1", "1234", "password123"]

for contraseña in contraseñas:
    if len(contraseña) < 8:
        print(f"La contraseña '{contraseña}' es demasiado corta.")
        break
else:
    print("Todas las contraseñas son suficientemente largas.")   
    
#  Verificar si todos los números en una lista son positivos:

numeros = [10, 20, 30, -5, 50]

for numero in numeros:
    if numero <= 0:
        print(f"El número {numero} no es positivo.")
        break
else:
    print("Todos los números son positivos.")   
    
       
    
