# This script generate a pdb movie with 
# proper coloring of corresponding PCA mode

from biopandas.pdb import PandasPdb
from generate_probability import generate_color_profile
from gmx_file_processing import match_col_in_int_list, read_ndx
from modes import shift_by_mode
import numpy as np
import sys

#def make_movie(input_pdb)

def change_bfactor_to_color(df, indices, color_profile):
    modify_items = ['b_factor']
    to_change = df.iloc[match_col_in_int_list(df, 'atom_number', indices)]
    color_values = to_change[modify_items]
    color_values = color_profile
    to_ret = to_change.copy()
    to_ret[modify_items] = color_values
    return to_ret

if __name__ == "__main__":
    # starting structure
    input_pdb = sys.argv[1]
    # index file
    input_index = sys.argv[2]
    # eigenvectors (modes)
    input_ev = np.load(sys.argv[3])
    # PCA mode
    mode = int(sys.argv[4])
    # output movie pdb
    movie_pdb = sys.argv[5]
    # biopandas dataframe
    ppdb = PandasPdb()
    ppdb.read_pdb(input_pdb)
    # generate color profile based on chosen mode
    color_profile = generate_color_profile(input_ev, mode)
    
    index = read_ndx(input_index)
    new_df = change_bfactor_to_color(ppdb.df['ATOM'], index['Protein'], color_profile)
    
    ppdb.to_pdb(movie_pdb)