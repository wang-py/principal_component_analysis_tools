import numpy as np
import sys
from pymol import cmd
from modes import get_xvg_stats
from generate_probability import generate_color_profile

if __name__ == "__main__":
    # xvg file that has the trajectory information
    xvgfile = sys.argv[1]
    # probability mode
    mode = int(sys.argv[2])
    # input pdb name
    input_pdb = sys.argv[3]
    # output pdb name
    movie_primer_pdb = sys.argv[4]

    color_profile = generate_color_profile(xvgfile, mode)
    for color in color_profile:
        # change the b factors of input pdb here
        cmd.alter("%s and ")

    #TODO: save the primer pdb here
    #cmd.save()