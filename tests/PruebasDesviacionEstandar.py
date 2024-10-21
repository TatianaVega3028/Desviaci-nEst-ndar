import unittest

from src.logica.DesviacionEstandar import DesviacionEstandar

class TestDesviacionEstandar(unittest.TestCase):
    def test_DesviacionEstandar_vacio_retornaNone(self):
        desviacionEstandar=DesviacionEstandar([])
        self.assertIsNone(desviacionEstandar,DesviacionEstandar())


if __name__ == '__main__':
    unittest.main()
