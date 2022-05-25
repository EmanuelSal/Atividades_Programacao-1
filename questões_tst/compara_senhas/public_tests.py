import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global compara_senhas
        undertest = __import__(module)
        compara_senhas = getattr(undertest, 'compara_senhas', None)

    def test_basico1(self):
       assert compara_senhas('aaa', 'bbb') == 3

    def test_basico2(self):
       assert compara_senhas('nome123', 'nome') == 0

    def test_basico3(self):
       assert compara_senhas('senha', 'Senha') == 1

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
