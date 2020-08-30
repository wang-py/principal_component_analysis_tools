#!/bin/bash

# starting index
START=$1

# ending index
STOP=$2

# filename prefix
FILENAME=mode

# separating pdb to initial pdb and xtc
for i in $( seq $START $STOP )
do
    # dump the first frame as a separate pdb
    echo 0 | gmx trjconv -f ${FILENAME}$i.pdb -s ${FILENAME}$i.pdb -dump 0 -o ${FILENAME}$i_1.pdb
    # convert the rest of movie to xtc
    echo 0 | gmx trjconv -f ${FILENAME}$i.pdb -s ${FILENAME}$i.pdb -b 1 -o ${FILENAME}$i.xtc
    # overwrite the original movie
    mv ${FILENAME}$i_1.pdb ${FILENAME}$i.pdb
done
