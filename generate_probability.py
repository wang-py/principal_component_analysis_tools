import sys
import numpy as np

def generate_probability_color_profile(eigenvectors, mode):
    # selected mode for output
    output_mode = eigenvectors[:, mode]
    # reshape the vector into N * 3 (N is number of residues)
    number_of_res = int(output_mode.shape[0] / 3)
    output_mode_reshaped = output_mode.reshape(number_of_res, 3)

    # find the probability vector by squaring the eigenvector
    probability_vec = np.square(output_mode_reshaped)

    # sum up three directions of probability components
    probability_by_res = np.sum(probability_vec, axis=1)

    # normalize by the maximum value
    probability_by_res_norm = probability_by_res / np.amax(probability_by_res)

    # finding cubic root
    probability_by_res_norm = np.cbrt(probability_by_res_norm)

    return probability_by_res_norm

# this function scans through the covariance matrix
# and generates one value for one atom
def get_one_correlation_value(cov_matrix, focus_atom, correlated_atom):
    x_f = cov_matrix[focus_atom - 1, :]
    y_f = cov_matrix[focus_atom, :]
    z_f = cov_matrix[focus_atom + 1, :]

# this function generates a color profile based on covariances of a chosen atom
# with every atom in the system
# cov_matrix: covariance matrix before diagonalization
# atom_number: atom to analyze
def generate_correlation_color_profile(cov_matrix, focus_atom_number):
    covariance_vector = cov_matrix[focus_atom_number - 1]

    return

def save_color_to_file(color_profile, filename):
    # write to output file
    output_file = open(filename, 'w')
    for one_res in color_profile:
        output_file.write(str(one_res) + "\n")

    output_file.close()

if __name__ == "__main__":
    # input xvg file
    xvgfile = sys.argv[1]
    # mode number
    mode = int(sys.argv[2])
    # output text file
    probability_file = sys.argv[3]
    color_profile = generate_probability_color_profile(xvgfile, mode)
    save_color_to_file(color_profile, probability_file)
