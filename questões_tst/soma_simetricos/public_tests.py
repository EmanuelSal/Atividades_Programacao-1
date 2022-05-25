import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global soma_simetricos
        undertest = __import__(module)
        soma_simetricos = getattr(undertest, 'soma_simetricos', None)

    def test_exemplo_1(self):
        assert soma_simetricos([2, 5, 3, 9]) == [11, 8]

    def test_exemplo_2(self):
        assert soma_simetricos([2, 5, 3, 9, 4]) == [6, 14, 3]



if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
