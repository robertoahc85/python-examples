# Desafío: Sistema de Gestión de Estudiantes
# Crea un programa en Python que gestione la información de los estudiantes de una escuela. 
# El programa debe permitir agregar nuevos estudiantes, mostrar la lista de estudiantes y buscar un estudiante por su nombre.

# Requisitos
# Funciones:

# agregar_estudiante(nombre, edad, grado): Agrega un nuevo estudiante a la lista.
# mostrar_estudiantes(): Muestra la lista completa de estudiantes.
# buscar_estudiante(nombre): Busca un estudiante por su nombre y muestra su información.
# Interacción con el Usuario:

# El programa debe mostrar un menú con las opciones: "Agregar estudiante", "Mostrar estudiantes", "Buscar estudiante" y "Salir".
# La opción "Agregar estudiante" debe pedir el nombre, edad y grado del estudiante.
# La opción "Mostrar estudiantes" debe mostrar la lista completa de estudiantes.
# La opción "Buscar estudiante" debe pedir el nombre del estudiante y mostrar su información si se encuentra en la lista.



estudiantes = []

def agregar_estudiante(nombre, edad, grado):
    estudiante = {
        'nombre': nombre,
        'edad': edad,
        'grado': grado
    }
    estudiantes.append(estudiante)

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes en la lista.")
    else:
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Grado: {estudiante['grado']}")

def buscar_estudiante(nombre):
    for estudiante in estudiantes:
        if estudiante['nombre'].lower() == nombre.lower():
            print(f"Estudiante encontrado:\nNombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Grado: {estudiante['grado']}")
            return
    print("Estudiante no encontrado.")

def mostrar_menu():
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Salir")

def gestionar_estudiantes():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = input("Ingrese la edad del estudiante: ")
            grado = input("Ingrese el grado del estudiante: ")
            agregar_estudiante(nombre, edad, grado)
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            nombre = input("Ingrese el nombre del estudiante: ")
            buscar_estudiante(nombre)
        elif opcion == '4':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Iniciar el programa
gestionar_estudiantes()
