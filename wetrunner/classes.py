import wcxf
from wcxf.util import qcd
from wetrunner import rge, definitions
from wetrunner.parameters import p as default_parameters
from collections import OrderedDict


class WET(object):
    """docstring for WET."""

    def __init__(self, wc, parameters=None):
        assert isinstance(wc, wcxf.WC)
        assert wc.basis == 'Bern', \
            "Wilson coefficients must be given in the 'Bern' basis"
        self.eft = wc.eft
        # number of quark flavours
        if self.eft == 'WET':
            self.f = 5
        elif self.eft == 'WET-4':
            self.f = 4
        elif self.eft == 'WET-3':
            self.f = 3
        self.scale_in = wc.scale
        self.C_in = wc.dict
        self.parameters = default_parameters
        if parameters is not None:
            self.parameters.update(parameters)

    @staticmethod
    def _betas(f):
        """QCD beta function for `f` dynamical quark flavours."""
        return (11*3 - 2*f)/3

    def _get_running_parameters(self, scale, f):
        p = {}
        p['alpha_s'] = qcd.alpha_s(scale, self.f, self.parameters['alpha_s'])
        p['m_b'] = qcd.m_b(self.parameters['m_b'], scale, self.f, self.parameters['alpha_s'])
        p['m_c'] = qcd.m_c(self.parameters['m_c'], scale, self.f, self.parameters['alpha_s'])
        # running ignored for alpha_e and lepton mass
        p['alpha_e'] = self.parameters['alpha_e']
        p['m_tau'] = self.parameters['m_tau']
        return p

    def run(self, scale_out, parameters=None, sectors='all'):
        pi = self._get_running_parameters(self.scale_in, self.f)
        po = self._get_running_parameters(scale_out, self.f)
        betas = self._betas(self.f)
        Etas = (pi['alpha_s'] / po['alpha_s'])
        if self.f != 5:  # for WET-4 and WET-3
            # to account for the fact that beta0 is hardcoded for f=5 in the
            # evolution matrices
            Etas = Etas**(self._betas(5) / self._betas(self.f))
            pi['alpha_e'] = 0  # because QED evolution is not consistent yet
        C_out = OrderedDict()
        for sector in wcxf.EFT[self.eft].sectors:
            if sector in definitions.sectors:
                if sectors == 'all' or sector in sectors:
                    C_out.update(rge.run_sector(sector, self.C_in,
                                 Etas, pi['alpha_s'], pi['alpha_e'],
                                 pi['m_b'], pi['m_c'], pi['m_tau'],
                                 betas))
        return wcxf.WC(eft='WET', basis='Bern',
                       scale=scale_out,
                       values=wcxf.WC.dict2values(C_out))
