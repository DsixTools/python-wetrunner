from wet_example_wc import Cdict
from adm import M
from definitions import C_keys, U_keys
from collections import OrderedDict

C_out = OrderedDict()

for i in range(5):
    for j in C_keys[i]:
        C_values = [Cdict.get(key, 0) for key in j]
        C_result = (M[U_keys[i][0]] + M[U_keys[i][1]]) @ C_values
        C_out[str(i+1)+", "+j[0][1:]] = C_result
        
