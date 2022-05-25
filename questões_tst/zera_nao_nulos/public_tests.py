import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global zera_nao_nulos
        undertest = __import__(module)
        zera_nao_nulos = getattr(undertest, 'zera_nao_nulos', None)

    def test_exemplo(self):
        jogo = [
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ]    
        zera_nao_nulos(jogo, 3, 2)
        assert jogo == [
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
        ]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
