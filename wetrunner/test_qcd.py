import unittest
from wetrunner.qcd import alpha_s

# All numbers compared to Mathemetica version of RunDec

delta = 1e-8


class TestQCD(unittest.TestCase):
    def test_alphas_invalid(self):
        with self.assertRaises(ValueError):
            alpha_s(100, 7)
        with self.assertRaises(ValueError):
            alpha_s(100, 2)
        with self.assertRaises(ValueError):
            alpha_s(100, 7)
        with self.assertRaises(ValueError):
            alpha_s(0, 6)
        with self.assertRaises(ValueError):
            alpha_s(-1, 6)
        with self.assertRaises(ValueError):
            alpha_s("1.0", 6)

    def test_alphas_5(self):
        self.assertAlmostEqual(alpha_s(100, 5),
                               0.11686431884237730186,
                               delta=delta)
        self.assertAlmostEqual(alpha_s(10, 5),
                               0.17931693160062720703,
                               delta=delta)
        # crazy values
        self.assertAlmostEqual(alpha_s(1, 5),
                               0.40957053067188524193,
                               delta=delta)
        self.assertAlmostEqual(alpha_s(1000, 5),
                               0.087076948997751428458,
                               delta=delta)

    def test_alphas_6(self):
        self.assertAlmostEqual(alpha_s(500, 6),
                               0.095517575136454583087,
                               delta=delta)
        # crazy values
        self.assertAlmostEqual(alpha_s(50, 6),
                               0.12785358110125187370,
                               delta=delta)


    def test_alphas_4(self):
        self.assertAlmostEqual(alpha_s(3, 4),
                               0.29435209052499102591,
                               delta=delta)
        # crazy values
        self.assertAlmostEqual(alpha_s(1, 4),
                               0.79002981710159579055,
                               delta=delta)
        self.assertAlmostEqual(alpha_s(1000, 4),
                               0.080189559551765940590,
                               delta=delta)


    def test_alphas_3(self):
        self.assertAlmostEqual(alpha_s(0.9, 3),
                               1.19919,
                               delta=1e-5)
        # crazy values
        self.assertAlmostEqual(alpha_s(1000, 3),
                               0.074837321203374316422,
                               delta=delta)
