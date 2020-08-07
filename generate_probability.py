from modes import get_xvg_stats
from modes import modes
import sys
import numpy as np

# input xvg file
xvgfile = sys.argv[1]
# mode number
mode = int(sys.argv[2])
# output text file
probability_file = sys.argv[3]

mean1, mean2, cov, s, u, v = get_xvg_stats(xvgfile)

# selected mode for output
output_mode = u[mode]
# reshape the vector into N * 3 (N is number of residues)
number_of_res = int(output_mode.shape[0] / 3)
output_mode_reshaped = output_mode.reshape(number_of_res, 3)

# find the probability vector by squaring the eigenvector
probaility_vec = np.square(output_mode_reshaped)

# sum up three directions of probability components
probaility_by_res = np.sum(probaility_vec, axis=1)

# write to output file