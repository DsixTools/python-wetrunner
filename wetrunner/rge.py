from wetrunner import evmat
from wetrunner.definitions import C_keys, U_keys
from collections import OrderedDict


def C_out(C_in, Etas, Alphas, Alphaem, mb, mc, mtau, betas):
    Cdictout = OrderedDict()
    for i in range(len(C_keys)):
        for keylist in C_keys[i]:
            args = Etas, Alphas, Alphaem, mb, mc, mtau, betas
            Us = getattr(evmat, U_keys[i][0])(*args)
            Ue = getattr(evmat, U_keys[i][1])(*args)
            C_input = [C_in.get(key, 0) for key in keylist]
            C_result = (Us + Ue) @ C_input
            for j in range(len(C_result)):
                Cdictout[keylist[j]] = C_result[j]
    return Cdictout
