import unittest
from miPrimeraAPI.web.funciones_auxiliares import calculariva
class test_calcular(unittest.TestCase):
    def test_calcular(self):
        self.assertEqual(calculariva(100),21)
        self.assertEqual(calculariva(1000),210)
        #self.assertEqual(calculariva(4371),124)
        self.assertEqual(calculariva(10000),2100)
if __name__ == '__main__':
    unittest.main()