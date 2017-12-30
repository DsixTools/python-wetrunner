import unittest
import wetrunner
import wcxf
import numpy as np

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


class TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.wc = get_random_wc('WET', 'Bern', 160)
        cls.wet = wetrunner.WET(cls.wc)

    def test_init(self):
        with self.assertRaises(AssertionError):
            wetrunner.WET(0)  # argument is not a WC instance

    def test_attr(self):
        self.assertEqual(self.wet.scale_in, 160)
        self.assertEqual(self.wet.C_in, self.wc.dict)

    def test_run(self):
        C_out = self.wet.run(4.2)
        # missing keys since sector Vb not implemented
        misskeys = [k for l in wetrunner.definitions.C52_keys for k in l]
        # assert all input WCs are present in the output
        # (not vice versa as RGE can generate them from zero)
        for k in self.wet.C_in:
            # only implemented for b-flavored WCs so far
            if 'b' in k and not 'dsbb' in k:
                if k not in misskeys:
                    self.assertTrue(k in C_out,
                                    msg='{} missing in output'.format(k))

    def test_wcxf(self):
        C_out = self.wet.run(4.2)
        wc = wcxf.WC('WET', 'Bern', 4.2, wcxf.WC.dict2values(C_out))
        wc.validate()

    def test_dump_wcxf(self):
        C_out = self.wet.run(4.2)
        wc = self.wet.dump_wcxf(C_out, 4.2)
        wc.validate()

    def test_run_wcxf(self):
        wc1 = self.wet.run_wcxf(4.2)
        C_out = self.wet.run(4.2)
        wc2 = self.wet.dump_wcxf(C_out, 4.2)
        self.assertEqual(wc1.eft, wc2.eft)
        self.assertEqual(wc1.basis, wc2.basis)
        self.assertEqual(wc1.scale, wc2.scale)
        self.assertDictEqual(wc1.dict, wc2.dict)
