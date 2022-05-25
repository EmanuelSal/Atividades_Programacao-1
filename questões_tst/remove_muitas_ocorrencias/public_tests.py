import unittest
import sys

module = sys.argv[-1].split(".py")[0]


class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_muitas_ocorrencias
        undertest = __import__(module)
        remove_muitas_ocorrencias = getattr(undertest, 'remove_muitas_ocorrencias', None)

    def test_example(self):
        l = [1, 1, 2, 1]
        assert remove_muitas_ocorrencias(l) == None
        assert l == [2]

    def test_exemplo2(self):
        l = [1, 2, 1, 2, 1, 1]
        assert remove_muitas_ocorrencias(l) == None
        assert l == [2, 2]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
