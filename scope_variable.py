def mi_funcion():
    x = 10  # x es local a mi_funcion
    print(x)

mi_funcion()
print(x)  # Esto causará un error porque x no está definido fuera de mi_funcion

#Alcance funcion
def mi_funcion(x):
    print(x)  # x es un parámetro de la función

mi_funcion(5)

#alcance Global
y = 20  # y es global
def mi_funcion():
    print(y)  # Se puede acceder a y desde dentro de la función

mi_funcion()
print(y)  # También se puede acceder a y desde fuera de la función

#alcance Modulo
z = 30  # z tiene alcance de módulo

def otra_funcion():
    print(z)  # z es accesible aquí

otra_funcion()
