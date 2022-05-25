import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global colapsa_n_menores 
        undertest = __import__(module)
        colapsa_n_menores = getattr(undertest, 'colapsa_n_menores', None)

    def test_exemplo(self):
        nums = [12, 3, 7, 1, 5, 10]
        colapsa_n_menores(3, nums)
        assert nums == [12, 7, 10, 9]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
