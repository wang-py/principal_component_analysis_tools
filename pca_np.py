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

def calculate_covariance_matrix(pos, pos_mean):
    return

if __name__ == "__main__":
    xvg_file = open(sys.argv[1], 'r')
    # use numpy array
    pos = np.array(read_xvg(xvg_file))
    pos_sum = np.sum(pos, axis=0)
    # manually averaging
    pos_mean = pos_sum / len(pos[:, 0])
