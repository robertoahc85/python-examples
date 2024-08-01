# Inicializar Listas
calificaciones_matematicas = [85, 90, 78]  # Calificaciones en Matemáticas
calificaciones_ciencias = [80, 88, 75]     # Calificaciones en Ciencias

# Calcular Promedios por Materia
promedio_matematicas = sum(calificaciones_matematicas) / len(calificaciones_matematicas)
promedio_ciencias = sum(calificaciones_ciencias) / len(calificaciones_ciencias)

# Calcular Promedios Generales por Estudiante
promedio_general_estudiante1 = (calificaciones_matematicas[0] + calificaciones_ciencias[0]) / 2
promedio_general_estudiante2 = (calificaciones_matematicas[1] + calificaciones_ciencias[1]) / 2
promedio_general_estudiante3 = (calificaciones_matematicas[2] + calificaciones_ciencias[2]) / 2

# Imprimir Resultados
print("Promedio en Matemáticas:", promedio_matematicas)
print("Promedio en Ciencias:", promedio_ciencias)
print("Promedio general del Estudiante 1:", promedio_general_estudiante1)
print("Promedio general del Estudiante 2:", promedio_general_estudiante2)
print("Promedio general del Estudiante 3:", promedio_general_estudiante3)
