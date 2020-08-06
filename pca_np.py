import numpy as np
import sys

def read_xvg(xvg_file):
    position = []
    lines = xvg_file.readlines()
    # data entry
    for line in lines:
        line_entry = line.split()
        # skip comments
        first_charactor = line_entry[0]
        if first_charactor[0] != '#' and first_charactor[0] != '@':
            # skip time data
            position.append(line_entry[1:])

    position_string = np.array(position)
    position_data = position_string.astype(np.float)
    return position_data

if __name__ == "__main__":
    xvg_file = open(sys.argv[1], 'r')
    # use numpy array
    pos = np.array(read_xvg(xvg_file))
    pos_sum = np.sum(pos, axis=0)
    # manually averaging
    pos_mean = pos_sum / len(pos[:, 0])
    # numpy covariance calculation
    pos_cov = np.cov(pos, rowvar=False)
    # eigen values calculation
    pos_eigval, pos_eigvector = np.linalg.eig(pos_cov)
    # shift the average to zero
    pos_shifted = pos - pos_mean
    # shifted covariance
    pos_shifted_cov = np.cov(pos_shifted, rowvar=False)
    # shifted eigenvalues
    pos_shifted_eig = np.linalg.eig(pos_shifted_cov)
