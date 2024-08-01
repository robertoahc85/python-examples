
# En , los operadores lógicos se utilizan para combinar condiciones o evaluar expresiones booleanas. Los tres operadores lógicos principales son:

# and
# or
# not
# 1. Operador and
# El operador and devuelve True solo si ambas condiciones son verdaderas.

# Ejemplo:

# 
# 
a = 10
b = 20
# Verifica si 'a' es mayor que 5 y 'b' es menor que 30
resultado = (a > 5) and (b < 30)
print(resultado)  # Output: True
# Explicación:

# (a > 5) es True porque 10 es mayor que 5.
# (b < 30) es True porque 20 es menor que 30.
# Como ambas condiciones son verdaderas, resultado es True.

# 2. Operador or
# El operador or devuelve True si al menos una de las condiciones es verdadera.

# Ejemplo:

x = 5
y = 15

# Verifica si 'x' es mayor que 10 o 'y' es menor que 20
resultado = (x > 10) or (y < 20)
print(resultado)  # Output: True
# Explicación:

# (x > 10) es False porque 5 no es mayor que 10.
# (y < 20) es True porque 15 es menor que 20.
# Como al menos una condición es verdadera, resultado es True.
# 3. Operador not
# El operador not invierte el valor de verdad de la condición. Si la condición es True, not la convierte en False, y viceversa.

# Ejemplo:



edad = 17

# Verifica si 'edad' no es mayor o igual a 18
resultado = not (edad >= 18)
print(resultado)  # Output: True
# Explicación:

# (edad >= 18) es False porque 17 no es mayor o igual a 18.
# not False es True, por lo que resultado es True.
# Combinación de Operadores
# Puedes combinar múltiples operadores lógicos en una sola expresión.

# Ejemplo:

a = 5
b = 15
c = 25

# Verifica si 'a' es menor que 10 y 'b' es menor que 20, o si 'c' es mayor que 20
resultado = ((a < 10) and (b < 20)) or (c > 20)
print(resultado)  # Output: True
# Explicación:

# (a < 10) es True y (b < 20) es True, por lo que (a < 10) and (b < 20) es True.
# (c > 20) es True porque 25 es mayor que 20.
# Como al menos una de las condiciones de la expresión principal es True, resultado es True.
# Estos operadores te permiten construir expresiones complejas para realizar decisiones más sofisticadas en tu código.

#and
a = True
b = False
resultado = a and b  # resultado será False porque b es False

#or
a = True
b = False
resultado = a or b  # resultado será True porque a es True

#not
a = True
resultado = not a  # resultado será False porque a es True


