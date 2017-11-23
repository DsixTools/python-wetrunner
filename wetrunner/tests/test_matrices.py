import wetrunner.adm
from wetrunner.adm import get_M, M
import numpy as np
import numpy.testing as npt
import json
from collections import OrderedDict
import unittest
import pkgutil

#"""check if the outputs are real"""
#for key in M.keys():
#    shape = M[key].shape
#    npt.assert_array_equal(M[key].imag, np.zeros(shape))


"""read json files"""
f = pkgutil.get_data('wetrunner', 'tests/data/random_par.json')
rpar = json.loads(f.decode('utf-8'))
f = pkgutil.get_data('wetrunner', 'tests/data/WETmatrixes.json')
Mat = json.loads(f.decode('utf-8'))


"""set values"""
Etas, Alphas, Alphaem, mb, mc, mtau, Betas = rpar
ma_results = OrderedDict()
i = 0
for key in M.keys():
    ma_results[key] = np.array(Mat[i])
    i+=1
py_results = get_M(Etas, Alphas, Alphaem, mb, mc, mtau, Betas)


"""tests"""
class TestMatrixes(unittest.TestCase):
    def test_matrixes(self):
        """keys"""
        self.assertEqual(ma_results.keys(), py_results.keys())
        for key in py_results.keys():
            """dimention of matrixes"""
            self.assertEqual(ma_results[key].shape, py_results[key].shape)
            """values of matrixes"""
            npt.assert_array_almost_equal(ma_results[key], py_results[key], decimal=3)

        """for UeV: to figure out the failed position: Output: (41, 40) 0.1->0.16"""
        for (index, value) in np.ndenumerate(py_results["UeV"]):
            self.assertAlmostEqual(ma_results["UeV"][index], py_results["UeV"][index], places=3,
                                   msg="Failed for index {}".format(index))


if __name__ == '__main__':
    unittest.main()
