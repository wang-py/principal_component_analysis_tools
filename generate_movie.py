# This script generate a pdb movie with 
# proper coloring of corresponding PCA mode

from biopandas.pdb import PandasPdb
from pca_coloring import generate_correlation_color_profile
from gmx_file_processing import match_col_in_int_list, read_ndx
from modes import shift_by_mode
import numpy as np
import sys
import os
import shutil

# change b factors into color values
def change_bfactor_to_color(df, indices, color_profile):
    modify_items = ['b_factor']
    to_change = df.iloc[match_col_in_int_list(df, 'atom_number', indices)]
    color_values = to_change[modify_items]
    color_values = color_profile
    to_ret = to_change.copy()
    to_ret[modify_items] = color_values
    return to_ret

# generate one frame of pdb movie
def render_one_frame(df, mode, indices, amplitude):
    mode = mode.reshape(int(len(mode) / 3), 3)
    stat_items=['x_coord', 'y_coord', 'z_coord']
    to_change = df.iloc[match_col_in_int_list(df,'atom_number',indices)]
    coords = to_change[stat_items]
    coords += mode * float(amplitude)
    frame_df = to_change.copy()
    frame_df[stat_items] = coords

    return frame_df

def make_buffer_folder(path):
    os.mkdir(path)

def rm_buffer(path):
    shutil.rmtree(path)

# combine individual frames into a complete pdb movie
def concatenate_pdbs(pdb_frame, frame_index, movie_pdb_file):
    # concatenation loop
    movie_pdb_file.write("TITLE    frame t= " + str(frame_index) +"\n")
    movie_pdb_file.write("MODEL    1\n")
    with open(pdb_frame, 'r') as f:
        movie_pdb_file.write(f.read())
    movie_pdb_file.write("TER\n")
    movie_pdb_file.write("ENDMDL\n")
    

# movie making function
def make_movie(df, output_pdb, mode, indices, amplitude, frames):
    buffer_folder = "movie_buffer"
    buffer_prefix = "frame"

    make_buffer_folder(buffer_folder)
    
    time_steps = np.linspace(float(0), float(frames), num = frames + 1)
    period = int(frames / 2)
    amplitude_frames = float(amplitude) * np.cos(np.pi * time_steps / period)
    movie = open(output_pdb, 'w')
    # movie making loop
    for i in range(len(amplitude_frames)):
        frame_df = render_one_frame(df, mode, indices, amplitude_frames[i])
        # save buffer pdb in the buffer folder
        frame_pdb = PandasPdb()
        frame_pdb.df['ATOM'] = frame_df
        pdb_filename = buffer_folder + "/" + buffer_prefix + str(i) + '.pdb'
        frame_pdb.to_pdb(pdb_filename, records=['ATOM'], \
            gz=False, append_newline=True)
        # combine buffers here
        concatenate_pdbs(pdb_filename, i, movie)
    # remove buffers
    movie.close()
    rm_buffer(buffer_folder)

if __name__ == "__main__":
    # starting structure
    input_pdb = sys.argv[1]
    # index file
    input_index = sys.argv[2]
    # eigenvectors (modes)
    input_ev = np.load(sys.argv[3])
    # PCA mode
    mode_index = int(sys.argv[4])
    mode = input_ev[:, mode_index]
    # covariance matrix
    input_cov = np.load(sys.argv[5])
    # output movie pdb
    movie_pdb = sys.argv[6]
    # biopandas dataframe
    ppdb = PandasPdb()
    ppdb.read_pdb(input_pdb)
    # generate color profile based on chosen mode
    # index of N2 cluster
    res_index = 1650
    color_profile = generate_correlation_color_profile(input_cov, res_index)
    
    index = read_ndx(input_index)
    colored_pdb_df = change_bfactor_to_color(ppdb.df['ATOM'], index['System'], color_profile)
    make_movie(colored_pdb_df, movie_pdb, mode, index['System'], 50, 200)
