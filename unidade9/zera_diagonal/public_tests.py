import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
zera_diagonal = getattr(undertest, 'zera_diagonal', None)

class PublicTests(unittest.TestCase):

    def test_1(self):
        m = [[8, 20, -7], [ 5, 1,  3], [ 6,  7, 9]]
        zera_diagonal(m)
        assert  m == [[0, 20, -7], [5, 0, 3], [6, 7, 0]]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
