import unittest

# Test Driven Development: generar los test primero
# y luego escribir el codigo necesario. Esto ayuda a 
# blindar el codigo.

# Este es un tipo de test de caja negra.
# En teoria no sabemos la implementacion
# pero sí, el input y el output esperado

def suma(num_1, num_2):
    # El abs() hará que tire un error
    return abs(num_1) + num_2

class CajaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado,  -17)

if __name__ == '__main__':
    unittest.main()