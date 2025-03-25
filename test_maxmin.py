import unittest
from main import selecao_maxmin

class TestMaxMinSelect(unittest.TestCase):
    def test_lista_com_um_elemento(self):
        self.assertEqual(selecao_maxmin([5]), (5, 5))
    
    def test_lista_com_dois_elementos(self):
        self.assertEqual(selecao_maxmin([3, 7]), (3, 7))
        self.assertEqual(selecao_maxmin([7, 3]), (3, 7))
    
    def test_lista_varios_elementos(self):
        self.assertEqual(selecao_maxmin([3, 5, 1, 9, 2, 8, 4, 7]), (1, 9))
        self.assertEqual(selecao_maxmin([-10, -5, 0, 5, 10]), (-10, 10))
        self.assertEqual(selecao_maxmin([100]), (100, 100))
    
    def test_lista_com_numeros_repetidos(self):
        self.assertEqual(selecao_maxmin([2, 2, 2, 2, 2]), (2, 2))
    
    def test_lista_com_numeros_negativos(self):
        self.assertEqual(selecao_maxmin([-1, -2, -3, -4, -5]), (-5, -1))

if __name__ == "__main__":
    unittest.main()
