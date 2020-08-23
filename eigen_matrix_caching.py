from modes import get_xvg_stats
import numpy as np
import sys

if __name__ == '__main__':
    unbias = sys.argv[3] if len(sys.argv)>3 else False
    pdbToAlign = sys.argv[2] if len(sys.argv)>2 else None
    mean1, mean2, cov, s, u, v = \
        get_xvg_stats(sys.argv[1],fitfile=pdbToAlign,unbias=unbias)
    with open('covariance.npy','wb') as f:
        np.save(f,cov)
    with open('eigenvectors.npy', 'wb') as f:
        np.save(f,u)