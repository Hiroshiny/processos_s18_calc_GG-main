import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_maior_numero_iguais(self):
        resultado = Calculadora.maiorNumero(5, 5)
        self.assertEqual(resultado, 'Os dois números são iguais')

    def test_maior_numero_primeiro_maior(self):
        resultado = Calculadora.maiorNumero(10, 5)
        self.assertEqual(resultado, 'O maior número é 10')

    def test_maior_numero_segundo_maior(self):
        resultado = Calculadora.maiorNumero(5, 10)
        self.assertEqual(resultado, 'O maior número é 10')

    def test_somar(self):
        resultado = Calculadora.somar(7, 3)
        self.assertEqual(resultado, 10)

    def test_diferenca(self):
        resultado = Calculadora.diferenca(5, 10)
        self.assertEqual(resultado, 5)

if __name__ == '__main__':
    unittest.main()