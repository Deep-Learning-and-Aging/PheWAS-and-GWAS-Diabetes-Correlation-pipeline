#!/bin/bash

list=()

for i in {1..22}; do
    list+=($i)
done

list+=(X)
list+=(Y)
list+=(XY)

for i in "${list[@]}"; do
    cp /n/groups/patel/uk_biobank/project_52887_genetics/ukb_imp_chr${i}_v3.bgen /n/scratch3/users/t/tad368/geno/chr${i}_v3.bgen

    echo "copied"

    echo "chr${i}_v3.bgen"

done
