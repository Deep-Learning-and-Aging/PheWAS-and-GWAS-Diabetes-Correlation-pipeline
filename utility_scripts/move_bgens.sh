#!/bin/bash

list=()

for i in {1..22}; do
    list+=($i)
done

list+=(X)
#list+=(Y) no Y chr in v3 bgen files
list+=(XY)

for i in "${list[@]}"; do

    echo "start copying chr${i}_v3.bgen"

    cp /n/groups/patel/uk_biobank/project_52887_genetics/ukb_imp_chr${i}_v3.bgen /n/scratch3/users/t/tad368/geno/chr${i}_v3.bgen

    echo "finished copying chr${i}_v3.bgen"
    echo ""

done
