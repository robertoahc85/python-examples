class Empleado:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
        self._salario = 0

    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"

    @property
    def email(self):
        return f"{self._nombre.lower()}.{self._apellido.lower()}@empresa.com"

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._salario = valor
        else:
            raise ValueError("El salario debe ser un número no negativo")

    @property
    def salario_anual(self):
        return self._salario * 12

    @property
    def impuestos(self):
        if self._salario < 1000:
            return 0
        elif 1000 <= self._salario < 2000:
            return self._salario * 0.1
        else:
            return self._salario * 0.2

# Uso de la clase
emp = Empleado("Juan", "Pérez")

# Uso de propiedades de solo lectura
print(emp.nombre_completo)  # Juan Pérez
print(emp.email)  # juan.perez@empresa.com

# Uso de propiedad con setter
emp.salario = 1500
print(emp.salario)  # 1500

# Intento de asignar un valor inválido
try:
    emp.salario = -1000
except ValueError as e:
    print(f"Error: {e}")

# Uso de propiedades calculadas
print(emp.salario_anual)  # 18000
print(emp.impuestos)  # 150.0

# Intento de modificar una propiedad de solo lectura
try:
    emp.nombre_completo = "Pedro Gómez"
except AttributeError as e:
    print(f"Error: {e}")