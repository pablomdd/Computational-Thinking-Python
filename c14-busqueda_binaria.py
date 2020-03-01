objetivo = int(input("Ingresa un numero: "))

epsilon = 0.01
piso =  0.0
techo = max(1.0, objetivo)

respuesta = (piso + techo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'piso = {piso}, techo = {techo}, respuesta = {respuesta}')
    if respuesta**2 < objetivo:
        piso = respuesta
    else:
        techo = respuesta
    respuesta = (piso + techo) / 2

print(f'La raiz cuadrada es {respuesta}')