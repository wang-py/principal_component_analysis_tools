# This script generate a pdb movie with 
# proper coloring of corresponding PCA mode

from biopandas.pdb import PandasPdb
from generate_probability import generate_color_profile
import sys

if __name__ == "__main__":
    # starting structure
    input_pdb = sys.argv[1]
    # eigenvectors (modes)
    input_ev = sys.argv[2]
    # PCA mode
    mode = int(sys.argv[3])
    # biopandas dataframe
    ppdb = PandasPdb()
    ppdb.read_pdb(input_pdb)
    # generate color profile based on chosen mode
    color_profile = generate_color_profile(input_ev, mode)
    
    for i in range(len(color_profile)):
        color = color_profile[i]
        ppdb.df['bfactor'][i] = color
    