# Ejemplos de manipulacion de cadenas
my_str = 'Pablomdd'

print(my_str)
print(len(my_str))

print(my_str[0]) 
# Los index funcionan: <inicio>:<fin>:<paso>
print(my_str[::2]) 

print(f"Mi arroba es {my_str}")
# Como funcionan las entradas (inputs)
nombre = input('Cuál es tu nomre?')

print(f"Hola {nombre}")

# Como funcionan los castings
edad =  int(input('Cuál es tu edad? '))
print(f"El tipo  de dato de edad es {type(edad)}")

# Reto: Longitud de un saludo
saludo = f"Hola, {nombre}!"
print(saludo)
print(f"La longitud del saludo es: {len(saludo)}")