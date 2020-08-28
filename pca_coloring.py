import sys
import numpy as np

def generate_probability_color_profile(mode):
    # reshape the vector into N * 3 (N is number of residues)
    number_of_res = int(mode.shape[0] / 3)
    mode_reshaped = mode.reshape(number_of_res, 3)

    # find the probability vector by squaring the eigenvector
    probability_vec = np.square(mode_reshaped)

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
    # indices of the focus atom
    f = [focus_atom, focus_atom + 1, focus_atom + 2]
    # indices of the correlated atom
    c = [correlated_atom, correlated_atom + 1, correlated_atom + 2]
    cor_sum = 0
    # scanning loop
    for fi in f:
        for ci in c:
            cor_sum += np.abs(cov_matrix[fi, ci])

    return cor_sum
    

# this function generates a color profile based on covariances of a chosen atom
# with every atom in the system
# cov_matrix: covariance matrix before diagonalization
# atom_number_index: atom to analyze, atom number - 1
def generate_correlation_color_profile(cov_matrix, focus_atom_number_index):
    atom_index_max = cov_matrix.shape[0]

    correlation_vector = []

    for i in range(0, atom_index_max, 3):
        one_correlation = get_one_correlation_value(cov_matrix, focus_atom_number_index * 3, i)
        correlation_vector.append(one_correlation)

    # normalize by the focus atom
    focus_atom_variance = correlation_vector[focus_atom_number_index]
    correlation_vector /= focus_atom_variance

    return correlation_vector

def save_color_to_file(color_profile, filename):
    # write to output file
    output_file = open(filename, 'w')
    for one_res in color_profile:
        output_file.write(str(one_res) + "\n")

    output_file.close()

if __name__ == "__main__":
    # input matrix file
    eigen_matrix_file = sys.argv[1]
    eigen_matrix = np.load(eigen_matrix_file)
    # mode number
    mode_index = int(sys.argv[2])
    mode = eigen_matrix[:, mode_index]
    # output text file
    probability_file = sys.argv[3]
    color_profile = generate_probability_color_profile(mode)
    save_color_to_file(color_profile, probability_file)
