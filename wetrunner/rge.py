from wetrunner import evmat
from wetrunner.definitions import sectors
from collections import OrderedDict    


def run_sector(sector, C_in, Etas, Alphas, Alphaem, mb, mc, mtau, betas):
    args = Etas, Alphas, Alphaem, mb, mc, mtau, betas
    Cdictout = OrderedDict()
    for classname, C_lists in sectors[sector].items():
        for i, keylist in enumerate(C_lists):
            Us = getattr(evmat, 'Us' + classname)(*args)
            Ue = getattr(evmat, 'Ue' + classname)(*args)
            C_input = [C_in.get(key, 0) for key in keylist]
            C_result = (Us + Ue) @ C_input
            for j in range(len(C_result)):
                Cdictout[keylist[j]] = C_result[j]
    return Cdictout
