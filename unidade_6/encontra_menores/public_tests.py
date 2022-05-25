import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
encontra_menores = getattr(undertest, 'encontra_menores', None)

class PublicTests(unittest.TestCase):

   def test_adicional_1(self):
      assert encontra_menores(3, [2,1,1,1,1,1]) == 2
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
