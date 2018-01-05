#This code was generated automatically by https://gitlab.lrz.de/ga45tac/cabbage/tree/master/for_WET/def_erzeuger.py

C1_keys, C2_keys, C3_keys, C4_keys, C51_keys, C52_keys, C53_keys, C61_keys, C62_keys, C63_keys, C64_keys, C65_keys, C66_keys, C67_keys,= [], [], [], [], [], [], [], [], [], [], [], [], [], []


# class 1
for qq in ['sb', 'db', 'ds']:
    # e.g. 1sbsb
    C1_keys.append(['{}{}{}'.format(i, qq, qq)
                    for i in ['1', '2', '3', '4', '5', '1p', '2p', '3p']])
U1_keys = ['UsI', 'UeI']


# class 2
for qq in ['cb', 'ub', 'us', 'cs', 'cd', 'ud']:
    for l in ['e', 'mu', 'tau']:
        for lp in ['e', 'mu', 'tau']:
            # e.g. 1cbemu
            C2_keys.append(['{}{}{}{}'.format(i, qq, l, lp)
                            for i in ['1', '5', '1p', '5p', '7p']])
U2_keys = ['UsII', 'UeII']

# class 3
for dd in ['sb', 'db', 'ds']:
    for uu in ['uc', 'cu']:
        for p in ['', 'p']:
            # e.g. 1sbuc
            C3_keys.append(['{}{}{}{}'.format(i, p, dd, uu)
                            for i in range(1, 11)])
U3_keys = ['UsIII', 'UeIII']

# class 4
for qq in ['sbsd', 'dbds']:
    for p in ['', 'p']:
        # e.g. 1sbsd
        C4_keys.append(['{}{}{}'.format(i, p, qq)
                        for i in range(1, 11, 2)])
U4_keys = ['UsIV', 'UeIV']

# class 5
for qq in ['sb', 'db']:
    for p in ['', 'p']:
        _C = []
        for pp in ['uu', 'dd', 'cc', 'ss', 'bb']:
            if pp[0] in qq:
                _C += ['{}{}{}{}'.format(i, p, qq, pp)
                       for i in range(1, 11, 2)]  # 1, 3, 5, 7, 9
            else:
                _C += ['{}{}{}{}'.format(i, p, qq, pp)
                       for i in range(1, 11)]  # 1, 2, ..., 10
        _C += ['7{}gamma{}'.format(p, qq),
               '8{}g{}'.format(p, qq)]
        for l in ['e', 'mu', 'tau']:
            # e.g. 1sbee
            _C += ['{}{}{}{}'.format(i, p, qq, 2 * l)
                   for i in range(1, 11, 2)]  # 1, 3, 5, 7, 9
        C51_keys.append(_C)
U5_keys = ['UsV', 'UeV']

# class 5b
for qq in ['sb', 'db']:
    for l in ['e', 'mu', 'tau']:
        for lp in ['e', 'mu', 'tau']:
            for p in ['', 'p']:
                C52_keys.append(['{}{}{}{}{}'.format(i, p, qq, l, lp)
                                 for i in range(1, 11, 2)])
U5b_keys = ['UsVb', 'UeVb']

# class 5nu
for qq in ['sb', 'db', 'ds']:
        for p in ['', 'p']:
            C53_keys.append(['nu1{}{}{}{}'.format(p, qq, l, lp)
                             for l in ['e', 'mu', 'tau']
                             for lp in ['e', 'mu', 'tau']])
U5nu_keys = ['UsVnu', 'UeVnu']

# #class 6a:
# U6a_keys = ['UsVIa', 'UeVIa']
#
# #class 6b:
# U6b_keys = ['UsVIb', 'UeVIb']
#
# #class 6c:
# U6c_keys = ['UsVIc', 'UeVIc']
#
# #class 6d:
# U6d_keys = ['UsVId', 'UeVId']
#
# #class 6e:
# U6e_keys = ['UsVIe', 'UeVIe']
#
# #class 6f:
# U6f_keys = ['UsVIf', 'UeVIf']
#
# #class 6g:
# U6g_keys = ['UsVIg', 'UeVIg']

U_keys = [U1_keys] + [U2_keys] + [U3_keys] + [U4_keys] + [U5_keys] + [U5b_keys] + [U5nu_keys]  #+ [U6a_keys] + [U6b_keys] + [U6c_keys] + [U6d_keys] + [U6e_keys] + [U6f_keys] + [U6g_keys]
C_keys = [C1_keys] + [C2_keys] + [C3_keys] + [C4_keys] + [C51_keys] + [C52_keys] + [C53_keys]  #+ [C61_keys] + [C62_keys] + [C63_keys] + [C64_keys] + [C65_keys] + [C66_keys] + [C67_keys]
