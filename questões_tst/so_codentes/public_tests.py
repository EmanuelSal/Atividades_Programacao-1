import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global so_coincidentes
        undertest = __import__(module)
        so_coincidentes = getattr(undertest, 'so_coincidentes', None)

    def test_semelhante_ao_da_prova_esq(self):
        M1 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

        M2= [[10, 11, 12],
             [13, 14, 15],
             [ 7,  8,  9]]

        assert so_coincidentes(M1, M2) == [[0,0,0],[0,0,0],[7,8,9]]

    def test_semelhante_ao_da_prova_dir(self):
        M1 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

        M3= [[ 1,  2,  3],
             [13, 14, 15],
             [16, 17, 18]]


        assert so_coincidentes(M1, M3) == [[1,2,3],[0,0,0],[0,0,0]]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
