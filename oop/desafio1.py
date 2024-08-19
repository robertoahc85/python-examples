class Empleado:
    contador_empleados = 0

    def __init__(self, nombre, salario, posicion):
        Empleado.contador_empleados += 1
        self._nombre = nombre
        self._id_unico = Empleado.contador_empleados
        self._salario = salario
        self._posicion = posicion

    def mostrar_informacion(self):
        return (f"ID: {self._id_unico}, Nombre: {self._nombre}, "
                f"Salario: {self._salario}, Posición: {self._posicion}")

    def actualizar_salario(self, nuevo_salario):
        self._salario = nuevo_salario

    def actualizar_posicion(self, nueva_posicion):
        self._posicion = nueva_posicion

    @classmethod
    def total_empleados(cls):
        return f"Total de empleados: {cls.contador_empleados}"

# Prueba del Desafío
empleado1 = Empleado("Juan Pérez", 50000, "Desarrollador")
empleado2 = Empleado("Ana Gómez", 60000, "Gerente de Proyecto")

print(empleado1.mostrar_informacion())
print(empleado2.mostrar_informacion())

# Actualizar el salario y la posición de un empleado
empleado1.actualizar_salario(55000)
empleado1.actualizar_posicion("Senior Developer")
print(empleado1.mostrar_informacion())

# Mostrar el número total de empleados
print(Empleado.total_empleados())
