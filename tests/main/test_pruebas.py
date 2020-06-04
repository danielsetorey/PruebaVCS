
from pruebas import suma


class TestSuma():
    def test_suma(self):
        assert suma(2, 2) == 4

    def test_suma2(self):
        assert suma(3, 2) == 5

    def test_suma3(self):
        assert suma(4, 2) == 6

