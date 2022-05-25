import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
multiplica_lista = getattr(undertest, 'multiplica_lista', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l = ['joao', 'pedro']
        assert multiplica_lista(2,l) == ['joao', 'pedro', 'joao', 'pedro']
    
    def test_exemplo(self):
        l  = [2]
        assert multiplica_lista(1,l) == [2]
   

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
