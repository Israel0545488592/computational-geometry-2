from trapazoidal_decomposition import *
import unittest

class Test(unittest.TestCase):

    def test_orient(self):

        vx1 = np.array([0, 0, 0])
        vx2 = np.array([0, 1, 0])
        vx3 = np.array([1, 0, 0])
        above = np.array([0, 0, 1])
        beneth = np.array([0, 0, -1])

        self.assertFalse(orient3D(vx1, vx2, vx3, above))
        self.assertTrue(orient3D(vx1, vx2, vx3, beneth))


if __name__ == '__main__':  unittest.main()