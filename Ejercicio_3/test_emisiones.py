
import unittest

from emisiones import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    def test_consumo_normal(self):
        resultado = calcular_emisiones_carbono(100)
        self.assertAlmostEqual(resultado, 40.0)

    def test_factor_emision_personalizado(self):
        resultado = calcular_emisiones_carbono(200, 0.5)
        self.assertAlmostEqual(resultado, 100.0)

    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0.0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)


if __name__ == "__main__":
    unittest.main()
