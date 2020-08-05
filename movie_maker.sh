#!/bin/bash

# this script cat all pdbs into a pymol-readable movie pdb
# Author: Panyue Wang, Email: pywang@ucdavis.edu

# output name
output="movie.pdb"
# frame number
frame=1

for pdb in `ls | sort -V`; do
    echo "TITLE     frame t= $frame" >> $output
    echo "MODEL         1" >> $output
    cat $pdb >> $output
    echo "TER" >> $output
    echo "ENDMDL" >> $output
    let $frame=$frame+1
done
