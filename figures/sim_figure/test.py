import sys
from different_code.Xorbas import Xorbas
sys.path.append("different_code")
sys.path.append("draw_pic")



xorbas = Xorbas()
k, l, g, r = xorbas.nkr_to_klgr(n, k, r)
DRC, NRC = xorbas.return_DRC_NRC(k, l, g, r, "best", 10, False)
