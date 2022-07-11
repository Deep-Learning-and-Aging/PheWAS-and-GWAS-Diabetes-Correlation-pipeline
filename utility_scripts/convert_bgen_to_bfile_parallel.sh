#!/bin/bash

list=()

for i in {1..22}; do
    list+=($i)
done

list+=("X")

for i in "${list[@]}"; do

    echo "started script for chr${i}_v3_bfile"

    sbatch ./convert_bgen_to_bfile.sh $i

done
