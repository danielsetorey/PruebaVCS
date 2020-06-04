import unittest
from pruebas import suma


class TestSuma(unittest.TestCase):
    def test_suma(self):
        assert suma(2, 2) == 4

    def test_suma2(self):
        assert suma(3, 2) == 5
