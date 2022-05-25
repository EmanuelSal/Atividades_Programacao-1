import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global diferenca_listas
        undertest = __import__(module)
        diferenca_listas = getattr(undertest, 'diferenca_listas', None)

    def test_exemplo(self):
        p1 = [2,1,3,4]
        p2 = [2]
        diferenca_listas(p1,p2) == [1,3,4]
        assert p1 == [1,3,4]

        p1 = [1,3,4]
        p2 = [4]
        diferenca_listas(p1,p2) == [1,3] 
        assert p1 == [1,3]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
