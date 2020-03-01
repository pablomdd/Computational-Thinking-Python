# Enumeración Exhaustiva es simplemente probar todas las posibilidades

# En este programa encontremos la raíz cuadrada de un entero
objetivo = int(input('Ingresa un entero: '))

repuesta = 0

while repuesta**2 < objetivo:
    print(repuesta)
    repuesta += 1

if repuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {repuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada')

