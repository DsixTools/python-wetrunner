import unittest
import wetrunner
from wetrunner import evmat
import wcxf
import numpy as np
import numpy.testing as npt

np.random.seed(112)


def get_random_wc(eft, basis, scale, cmax=1e-2):
    """Generate a random wcxf.WC instance for a given basis."""
    basis_obj = wcxf.Basis[eft, basis]
    _wc = {}
    for s in basis_obj.sectors.values():
        for name, d in s.items():
            _wc[name] = cmax * np.random.rand()
            if 'real' not in d or not d['real']:
                _wc[name] += 1j * cmax * np.random.rand()
    return wcxf.WC(eft, basis, scale, wcxf.WC.dict2values(_wc))


class TestDef(unittest.TestCase):

    def test_sectors(self):
        for sname, sdict in wetrunner.definitions.sectors.items():
            # there should only be one class per sector
            self.assertEqual(len(list(sdict.keys())), 1)
            self.assertIn(sname, wcxf.Basis['WET', 'Bern'].sectors.keys())
            for cname, clists in sdict.items():
                for clist in clists:
                    for c in clist:
                        allkeys = wcxf.Basis['WET', 'Bern'].sectors[sname].keys()
                        self.assertIn(c, allkeys)


class TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.wc = get_random_wc('WET', 'Bern', 160)
        cls.wet = wetrunner.WETrunner(cls.wc)

    def test_init(self):
        with self.assertRaises(AssertionError):
            wetrunner.WETrunner(0)  # argument is not a WC instance
        wcf = get_random_wc('WET', 'flavio', 160)  # wrong basis
        with self.assertRaises(AssertionError):
            wetrunner.WETrunner(wcf)

    def test_attr(self):
        self.assertEqual(self.wet.scale_in, 160)
        self.assertEqual(self.wet.C_in, self.wc.dict)

    def test_wcxf(self):
        wc = self.wet.run(4.2)
        wc.validate()

    def test_run(self):
        C_out = self.wet.run(4.2).dict
        # assert all input WCs are present in the output
        # (not vice versa as RGE can generate them from zero)
        for k in self.wet.C_in:
            # ignore ds-flavored operators except sdnunu
            if ('ds' not in k and 'sd' not in k) or 'nu' in k:
                self.assertTrue(k in C_out,
                                msg='{} missing in output'.format(k))


class TestEvolutionMatrices(unittest.TestCase):
    def test_inverse_s(self):
        # check inverse of QCD evolution matrices
        args = (0.12, 1/128, 4.2, 1.2, 0.1, 0.106, 1.77, 23/3)
        npt.assert_array_almost_equal(evmat.UsI(0.123, *args),
                                      np.linalg.inv(evmat.UsI(1/0.123, *args)))
        npt.assert_array_almost_equal(evmat.UsII(0.123, *args),
                                      np.linalg.inv(evmat.UsII(1/0.123, *args)))
        npt.assert_array_almost_equal(evmat.UsIII(0.123, *args),
                                      np.linalg.inv(evmat.UsIII(1/0.123, *args)))
        npt.assert_array_almost_equal(evmat.UsIV(0.123, *args),
                                      np.linalg.inv(evmat.UsIV(1/0.123, *args)))
        npt.assert_array_almost_equal(evmat.UsV(0.123, *args),
                                      np.linalg.inv(evmat.UsV(1/0.123, *args)))
        npt.assert_array_almost_equal(evmat.UsVdeltaS(0.123, *args)
                                      @ evmat.UsVdeltaS(1/0.123, *args),
                                      np.eye(57),
                                      decimal=1)  # FIXME not precise enough!
        npt.assert_array_almost_equal(evmat.UsVb(0.123, *args),
                                      np.linalg.inv(evmat.UsVb(1/0.123, *args)))


class TestClassWET4(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.wc = get_random_wc('WET-4', 'Bern', 4)
        cls.wet = wetrunner.WETrunner(cls.wc)

    def test_wcxf(self):
        wc = self.wet.run(1.2)
        wc.validate()

    def test_run(self):
        C_out = self.wet.run(1.2).dict
        # assert all input WCs are present in the output
        # (not vice versa as RGE can generate them from zero)
        for k in self.wet.C_in:
            # ignore ds-flavored operators except sdnunu
            self.assertTrue(k in C_out,
                            msg='{} missing in output'.format(k))
