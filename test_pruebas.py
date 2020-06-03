import unittest
from pruebas import suma


class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 2), 4)


