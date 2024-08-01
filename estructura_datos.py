# Listas (list)
frutas = ["manzana", "banana", "cereza"]
numeros = [1, 2, 3, 4, 5]
print(type(frutas))  # Output: <class 'list'>

frutas = ["manzana", "banana", "cereza"]
print(frutas[0])  # Output: manzana

# Modificar un elemento
frutas[1] = "naranja"
print(frutas)  # Output: ['manzana', 'naranja', 'cereza']

# Agregar un elemento
frutas.append("kiwi")
print(frutas)  # Output: ['manzana', 'naranja', 'cereza', 'kiwi']



# Tuplas (tuple)
dimensiones = (1920, 1080)
coordenadas = (10, 20)
print(type(dimensiones))  # Output: <class 'tuple'>

punto = (10, 20)
print(punto[1])  # Output: 20

# Intentar modificar un elemento (esto generará un error)
# punto[1] = 30  # TypeError: 'tuple' object does not support item assignment



# Conjuntos (set)
colores = {"rojo", "verde", "azul"}
numeros_unicos = {1, 2, 3, 3, 4}
print(type(colores))  # Output: <class 'set'>

numeros = {1, 2, 3, 4, 5}
print(numeros)  # Output: {1, 2, 3, 4, 5}

# Agregar un elemento
numeros.add(6)
print(numeros)  # Output: {1, 2, 3, 4, 5, 6}

# Eliminar un elemento
numeros.remove(3)
print(numeros)  # Output: {1, 2, 4, 5, 6}

numeros2 = {2, 2, 3, 4, 4}
len(numeros2) #regresa 3 de len



# Diccionarios (dict)
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
precios = {"manzana": 1.2, "banana": 0.8, "cereza": 2.5}
print(type(persona))  # Output: <class 'dict'>

# NoneType
variable_no_definida = None
print(type(variable_no_definida))  # Output: <class 'NoneType'>

persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
print(persona["nombre"])  # Output: Ana

# Modificar un valor
persona["edad"] = 31
print(persona)  # Output: {'nombre': 'Ana', 'edad': 31, 'ciudad': 'Madrid'}

# Agregar un nuevo par clave-valor
persona["ocupacion"] = "Ingeniera"
print(persona)  # Output: {'nombre': 'Ana', 'edad': 31, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniera'}
