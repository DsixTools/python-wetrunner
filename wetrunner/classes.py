import wcxf
from wcxf.util import qcd
from wetrunner import rge
from wetrunner.parameters import p as default_parameters

class WET(object):
    """docstring for WET."""

    def __init__(self, wc, parameters=None):
        assert isinstance(wc, wcxf.WC)
        self.scale_in = wc.scale
        self.C_in = wc.dict
        self.parameters = default_parameters
        if parameters is not None:
            self.parameters.update(parameters)

    def _get_running_parameters(self, scale, f):
        p = {}
        p['alpha_s'] = qcd.alpha_s(scale, f, self.parameters['alpha_s'])
        p['m_b'] = qcd.m_b(self.parameters['m_b'], scale, f, self.parameters['alpha_s'])
        p['m_c'] = qcd.m_b(self.parameters['m_c'], scale, f, self.parameters['alpha_s'])
        # running ignored for alpha_e and lepton mass
        p['alpha_e'] = self.parameters['alpha_e']
        p['m_tau'] = self.parameters['m_tau']
        return p

    def run(self, scale_out, parameters=None):
        f = 5
        pi = self._get_running_parameters(self.scale_in, f)
        po = self._get_running_parameters(scale_out, f)
        Etas = pi['alpha_s'] / po['alpha_s']
        betas = (11*3 - 2*f)/3
        C_out = rge.C_out(self.C_in,
                          Etas, pi['alpha_s'], pi['alpha_e'],
                          pi['m_b'], pi['m_c'], pi['m_tau'],
                          betas)
        return wcxf.WC(eft='WET', basis='Bern',
                       scale=scale_out,
                       values=wcxf.WC.dict2values(C_out))
