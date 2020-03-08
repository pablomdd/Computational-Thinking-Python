# Note that this is a very inneficient implementation

def fibonacci(n):

    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Ingresa el n-esimo termino de fibonacci para calcular: '))

print(fibonacci(n))