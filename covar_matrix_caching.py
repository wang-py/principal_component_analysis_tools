from modes import get_xvg_stats
import numpy as np
import sys

if __name__ == '__main__':
    unbias = sys.argv[3] if len(sys.argv)>3 else False
    pdbToAlign = sys.argv[2] if len(sys.argv)>2 else None
    mean1, mean2, cov, s, u, v = \
        get_xvg_stats(sys.argv[1],fitfile=pdbToAlign,unbias=unbias)
    np.set_printoptions(threshold=sys.maxsize)
    np.core.arrayprint._line_width = 1800
    #print("mean ",mean1)
    #print("cov ", cov.shape)
    #print("D ", s.shape)
    #print("S ", u.shape)
    #print("S2 ",v.shape)
    #print("sum(S-S2)=",np.sum(u-v))
    #print("D = ", s)
    with open('eigenvalues.npy','wb') as f:
        np.save(f,s)
    with open('eigenvectors.npy', 'wb') as f:
        np.save(f,u)