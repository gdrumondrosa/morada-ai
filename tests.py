import unittest
from saque import calcular_cedulas

class TestCaixaEletronico(unittest.TestCase):
    def test_saque(self):
        self.assertEqual(calcular_cedulas(380), {100: 3, 50: 1, 20: 1, 10: 1, 5: 0, 2: 0})
        self.assertEqual(calcular_cedulas(246), {100: 2, 50: 0, 20: 2, 10: 0, 5: 0, 2: 3})
        self.assertEqual(calcular_cedulas(100), {100: 1, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0})
        self.assertEqual(calcular_cedulas(7), {100: 0, 50: 0, 20: 0, 10: 0, 5: 1, 2: 1})
        self.assertEqual(calcular_cedulas(4), {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 2})
        self.assertEqual(calcular_cedulas(1), "Valor de saque não pode ser atendido com as cédulas disponíveis.")

if __name__ == '__main__':
    unittest.main()
