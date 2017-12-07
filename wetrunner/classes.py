import wcxf
from . import rge
from . import qcd

class WET(object):
    """docstring for WET."""
    def __init__(self, wc):
        assert isinstance(wc, wcxf.WC)
        self.scale_in = wc.scale
        self.C_in = wc.dict
        self.parameters = self._get_parameters(self.scale_in)

    def _get_parameters(self, scale):
        return {'m_b': 4.2, 'm_c': 1.2, 'm_tau': 1.777, 'alpha_s': 0.1185}

    def run(self, scale):
        alphas_in = self.parameters['alpha_s']
        alphae_in = self.parameters['alpha_e']
        alphas_out = rge.alpha_s(scale, n_flav=5)
        Etas = alphas_in/alphas_out
        mb = self.parameters['m_b']
        mc = self.parameters['m_c']
        mtau = self.parameters['m_tau']
        return rge.C_out(self.C_in, Etas, alphas_in, alphae_in, mb, mc, mtau)
        
        
    