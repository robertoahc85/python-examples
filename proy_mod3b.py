# Estructura principal
tareas = []

def mostrar_menu():
    print("\n--- Menú de Gestión de Tareas ---")
    print("1. Agregar una tarea")
    print("2. Marcar una tarea como completada")
    print("3. Eliminar una tarea")
    print("4. Listar todas las tareas")
    print("5. Salir")

def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha = input("Ingrese la fecha de vencimiento (dd/mm/aaaa): ")
    tarea = {"descripcion": descripcion, "fecha": fecha, "completada": False}
    tareas.append(tarea)
    print(f"Tarea '{descripcion}' agregada correctamente.")

def marcar_completada():
    descripcion = input("Ingrese la descripción de la tarea a marcar como completada: ")
    for tarea in tareas:
        if tarea["descripcion"].lower() == descripcion.lower():
            if not tarea["completada"]:
                tarea["completada"] = True
                print(f"Tarea '{descripcion}' marcada como completada.")
            else:
                print(f"La tarea '{descripcion}' ya está completada.")
            return
    print("Tarea no encontrada.")

def eliminar_tarea():
    descripcion = input("Ingrese la descripción de la tarea a eliminar: ")
    for tarea in tareas:
        if tarea["descripcion"].lower() == descripcion.lower():
            tareas.remove(tarea)
            print(f"Tarea '{descripcion}' eliminada.")
            return
    print("Tarea no encontrada.")

def listar_tareas():
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        for tarea in tareas:
            estado = 'Completada" si tarea["completada"] else "Pendiente'
            print(f"Descripción: {tarea['descripcion']}, Fecha: {tarea['fecha']}, Estado: {estado}")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            marcar_completada()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            listar_tareas()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el programa
ejecutar_programa()
