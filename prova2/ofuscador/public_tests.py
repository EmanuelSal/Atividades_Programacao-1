import unittest
import sys

module = sys.argv[-1].split(".py")[0]


class PublicTests(unittest.TestCase):

   @classmethod
   def setUpClass(cls):
      global ofuscador
      undertest = __import__(module)
      ofuscador = getattr(undertest, 'ofuscador', None)

   def test_exemplo_1(self):
      assert ofuscador("I love Python!") == "1*70V3****pYTH0N!"



if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
