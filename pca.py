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

    return position

if __name__ == "__main__":
    xvg_file = open(sys.argv[1], 'r')
    pos = read_xvg(xvg_file)
