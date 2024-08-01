# 1. Lista de nombres
nombres = ["Ana", "Carlos", "Elena", "David", "Beatriz"]

# 2. Lista de edades
edades = [18, 20, 19, 22, 21]

# 3. Lista de calificaciones
calificaciones = [75, 45, 90, 60, 88]

# 4. Promedio de edades
promedio_edad = sum(edades) / len(edades)

# 5. Promedio de calificaciones
promedio_calificacion = sum(calificaciones) / len(calificaciones)

# 6. Lista de aprobados
aprobados = [calificacion >= 60 for calificacion in calificaciones]

# 7. Mejor estudiante
mejor_estudiante = nombres[calificaciones.index(max(calificaciones))]

# 8. Peor estudiante
peor_estudiante = nombres[calificaciones.index(min(calificaciones))]

# 9. Todos aprobados
todos_aprobados = all(aprobados)

# 10. Reporte
reporte = f"""Promedio de edad: {promedio_edad:.2f}
Promedio de calificación: {promedio_calificacion:.2f}
Mejor estudiante: {mejor_estudiante}
Peor estudiante: {peor_estudiante}
Todos aprobados: {todos_aprobados}"""

# 11. Imprimir reporte
print(reporte)