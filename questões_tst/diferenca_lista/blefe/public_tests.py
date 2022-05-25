import unittest
import sys

module = sys.argv[-1].split(".py")[0]


class PublicTests(unittest.TestCase):

   @classmethod
   def setUpClass(cls):
      global blefe
      undertest = __import__(module)
      blefe = getattr(undertest, 'blefe', None)

   def test_exemplo_1(self):
      l1 = [9, 4, 5, 3, 1]
      assert blefe(l1) == [0, 0, 1, 0, 0]
      assert l1 == [9, 4, 4, 3, 1]

   def test_exemplo_2(self):
      l2 = [15, 9, 4, 5, 2, 1, 3, 4]
      assert blefe(l2) == [0, 0, 0, 1, 0, 0, 2, 3]
      assert l2 == [15, 9, 4, 4, 2, 1, 1, 1]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
