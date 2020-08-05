#!/bin/bash

# this script cat all pdbs into a pymol-readable movie pdb
# Author: Panyue Wang, Email: pywang@ucdavis.edu

output="movie.pdb"

for pdb in `ls | sort -V`; do
    cat $pdb >> $output
done
