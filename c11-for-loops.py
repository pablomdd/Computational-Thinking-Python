# Uso de for en python
frutas = ['manzana', 'pera', 'mango']
for fruta in frutas:
        print(fruta)

# Un iterator funciona sobre un objeto iterable
# iter() guarda el estado del iterable
iterador = iter(frutas)
print(next(iterador))
# manzana
print(next(iterador))
# pera
print(next(iterador))
# mango

# Iterar en dicionarios
estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4
}

# imprime los keys
for pais in estudiantes:
    print(pais)
# vuelve a imprimir los keys
for pais in estudiantes.keys():
    print(pais)
# imprime los values
for pais in estudiantes.values():
    print(pais)
# imprime tanto los keys como los values
for pais, numero_de_estudiantes in  estudiantes.items():
    print(pais,numero_de_estudiantes)

