#!/bin/bash

# this script cat all pdbs into a pymol-readable movie pdb
# Author: Panyue Wang, Email: pywang@ucdavis.edu

# working directory

DIR=$1

# output name
output=$2
# frame number
frame=1

input=`ls $DIR | sort -V`

for pdb in $input; do
    echo "TITLE     frame t= $frame" >> $output
    echo "MODEL         1" >> $output
    cat $DIR/$pdb >> $output
    echo "TER" >> $output
    echo "ENDMDL" >> $output
    let frame=frame+1
done
