import rundec

crd = rundec.CRunDec()

def alpha_s(scale):
    """3-loop cumputation of alpha_s for 5 and less flavours
    with initial condition alpha_s(MZ) = 0.1185
    or alpha_s(mc) = 0.505999      """
    loop = 3
    alphasMZ = 0.1185
    MZ = 91.1876
    mc = 1.2
    alphamc = 0.505999
    if scale > 4.18:
        f = 5
        return crd.AlphasExact(alphasMZ, MZ, scale, f, loop)
    elif scale > 1.2:
        f = 4
        return crd.AlphasExact(alphasMZ, MZ, scale, f, loop)
    elif scale > 0.95:
        f = 3
        return crd.AlphasExact(alphamc, mc, scale, f, loop)
    elif scale > 0.48:
        f = 2
        return crd.AlphasExact(alphamc, mc, scale, f, loop)
    else:
        return "only one flavour"
