from wetrunner import evmat
from wetrunner.definitions import C_keys, U_keys
from collections import OrderedDict

def C_out(C_in, Etas, Alphas, Alphaem, mb, mc, mtau):
    Cdictout = OrderedDict()
    for i in range(5):
        for j in C_keys[i]:
            args = Etas, Alphas, Alphaem, mb, mc, mtau
            Us = getattr(evmat, U_keys[i][0])(*args)
            Ue = getattr(evmat, U_keys[i][1])(*args)
            C_in = [C_in.get(key, 0) for key in j]
            C_result = (Us + Ue) @ C_in
            for k in range(len(C_result)):
                Cdictout[j[k]] = C_result[k]
    return Cdictout
