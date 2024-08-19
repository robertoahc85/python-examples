class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre      # Público
        self._departamento = None # Protegido
        self.__salario = salario  # Privado
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario debe ser positivo")
    
    def _asignar_departamento(self, departamento):
        self._departamento = departamento
    
    def __calcular_bonus(self):
        return self.__salario * 0.1

# Uso de la clase
emp = Empleado("Ana", 50000)
print(emp.nombre)           # Acceso directo a atributo público
emp.salario = 55000         # Uso de setter
print(emp.salario)          # Uso de getter
emp._asignar_departamento("Ventas")  # Uso de método protegido
# print(emp.__salario)      # Esto generaría un error
# emp.__calcular_bonus()    # Esto también generaría un error