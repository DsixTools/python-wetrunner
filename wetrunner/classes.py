import wcxf
from wetrunner import rge, qcd, parameters

class WET(object):
    """docstring for WET."""
    def __init__(self, wc):
        assert isinstance(wc, wcxf.WC)
        self.scale_in = wc.scale
        self.C_in = wc.dict
        self.p = self._get_parameters(self.scale_in)

    def _get_parameters(self, scale):        
        return parameters.p

    def run(self, scale_out, 
            alphas_in = parameters.p['alpha_s'], 
            alphae_in = parameters.p['alpha_e'], 
            mb = parameters.p['m_b'], 
            mc = parameters.p['m_c'], 
            mtau = parameters.p['m_tau'], 
            betas = parameters.p['betas']):
        alphas_out = qcd.alpha_s(scale_out, n_flav=5)
        Etas = alphas_in/alphas_out
        return rge.C_out(self.C_in, Etas, alphas_in, alphae_in, mb, mc, mtau, betas)
        
    def run_wcxf(self, scale_out,
                  alphas_in = parameters.p['alpha_s'], 
                  alphae_in = parameters.p['alpha_e'], 
                  mb = parameters.p['m_b'], 
                  mc = parameters.p['m_c'], 
                  mtau = parameters.p['m_tau'], 
                  betas = parameters.p['betas']):
         alphas_out = qcd.alpha_s(scale_out, n_flav=5)
         Etas = alphas_in/alphas_out
         return wcxf.WC(eft = 'WET', basis = 'AFGV', scale = scale_out, values = wcxf.WC.dict2values(rge.C_out(self.C_in, Etas, alphas_in, alphae_in, mb, mc, mtau, betas)))
        
    def dump_wcxf(self, C, scale_out):
        return wcxf.WC(eft = 'WET', basis = 'AFGV', scale = scale_out, values = wcxf.WC.dict2values(C))