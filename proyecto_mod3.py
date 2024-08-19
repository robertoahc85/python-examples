# Estructura principal
libros = []

def mostrar_menu():
    print("\n--- Menú Biblioteca Digital ---")
    print("1. Agregar un libro")
    print("2. Buscar un libro")
    print("3. Listar todos los libros")
    print("4. Registrar un préstamo")
    print("5. Registrar una devolución")
    print("6. Salir")

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = input("Ingrese el año de publicación: ")
    libro = {"titulo": titulo, "autor": autor, "año": año, "prestado": False}
    libros.append(libro)
    print(f"Libro '{titulo}' agregado correctamente.")

def buscar_libro():
    titulo = input("Ingrese el título del libro que busca: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            print(f"Encontrado: {libro}")
            return
    print("Libro no encontrado.")

def listar_libros():
    if not libros:
        print("No hay libros en la biblioteca.")
    else:
        for libro in libros:
            estado = "Prestado" if libro["prestado"] else "Disponible"
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}, Estado: {estado}")

def registrar_prestamo():
    titulo = input("Ingrese el título del libro a prestar: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if not libro["prestado"]:
                libro["prestado"] = True
                print(f"Libro '{titulo}' prestado exitosamente.")
            else:
                print(f"El libro '{titulo}' ya está prestado.")
            return
    print("Libro no encontrado.")

def registrar_devolucion():
    titulo = input("Ingrese el título del libro a devolver: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["prestado"]:
                libro["prestado"] = False
                print(f"Libro '{titulo}' devuelto exitosamente.")
            else:
                print(f"El libro '{titulo}' no estaba prestado.")
            return
    print("Libro no encontrado.")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_libro()
        elif opcion == "3":
            listar_libros()
        elif opcion == "4":
            registrar_prestamo()
        elif opcion == "5":
            registrar_devolucion()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el programa
ejecutar_programa()
