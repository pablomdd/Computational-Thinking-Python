# Funciones como argumentos de otras funciones
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    print(resultados)

nums = [1, 2, 3]
aplicar_operacion(multiplicar_por_dos, nums)

aplicar_operacion(sumar_dos, nums)

# Funciones Lamda
suma = lambda x, y: x + y

print(suma(3,5))

# Funciones en estructuras de datos

def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

print(aplicar_operaciones(-2))


