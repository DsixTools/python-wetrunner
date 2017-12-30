import rundec

crd = rundec.CRunDec()

def alpha_s(scale, f, alphasMZ=0.1185):
    """3-loop cumputation of alpha_s for f flavours
    with initial condition alpha_s(MZ) = 0.1185"""
    if not isinstance(scale, (float, int)) or scale <= 0:
        raise ValueError("Scale must be a positive number")
    if not isinstance(f, int) and 3 <= f <= 6:
        raise ValueError("f must be an integer between 3 and 6")
    loop = 3
    MZ = 91.1876
    if f == 5:
        return crd.AlphasExact(alphasMZ, MZ, scale, f, loop)
    elif f == 6:
        crd.nfMmu.Mth = 170
        crd.nfMmu.muth = 170
        crd.nfMmu.nf = 6
        return crd.AlL2AlH(alphasMZ, MZ, crd.nfMmu, scale, loop)
    elif f == 4:
        crd.nfMmu.Mth = 4.8
        crd.nfMmu.muth = 4.8
        crd.nfMmu.nf = 4
        return crd.AlH2AlL(alphasMZ, MZ, crd.nfMmu, scale, loop)
    elif f == 3:
        crd.nfMmu.Mth = 4.8
        crd.nfMmu.muth = 4.8
        crd.nfMmu.nf = 4
        mc = 1.3
        asmc =  crd.AlH2AlL(alphasMZ, MZ, crd.nfMmu, mc, loop)
        crd.nfMmu.Mth = mc
        crd.nfMmu.muth = mc
        crd.nfMmu.nf = 3
        return crd.AlH2AlL(asmc, mc, crd.nfMmu, scale, loop)
    else:
        raise ValueError("Running only implemented for 3 <= f <= 6")
