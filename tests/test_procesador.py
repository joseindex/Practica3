import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        self.assertEqual(total_provincias, 24)

    def test_ventas_totales_mayores_5k(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertTrue(all(float(v) > 5000 for v in resumen.values()))

    def test_ventas_por_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Narnia")

    def test_ventas_por_provincia_existente(self):
        resultado = self.analizador.ventas_por_provincia("pichincha")
        self.assertGreater(resultado, 0)



    def test_exportaciones_totales_por_mes(self):
        analizador = Analizador("datos/sri_ventas_2024.csv")
        resultado = analizador.exportaciones_totales_por_mes()
        self.assertIsInstance(resultado, dict)
        self.assertIn("ENERO", resultado)
        self.assertIn("FEBRERO", resultado)
        self.assertIsInstance(resultado["ENERO"], float)




    def test_porcentaje_tarifa_0_por_provincia(self):
        analizador = Analizador("datos/sri_ventas_2024.csv")
        resultado = analizador.porcentaje_tarifa_0_por_provincia()
        self.assertIsInstance(resultado, dict)
        self.assertIn("PICHINCHA", resultado)
        self.assertIn("GUAYAS", resultado)
        self.assertIsInstance(resultado["PICHINCHA"], float)
        self.assertGreaterEqual(resultado["PICHINCHA"], 0)


