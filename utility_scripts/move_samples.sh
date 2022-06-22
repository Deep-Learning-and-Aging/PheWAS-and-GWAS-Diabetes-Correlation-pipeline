#!/bin/bash

list=()

for i in {1..22}; do
    list+=($i)
done

list+=(X)

for i in "${list[@]}"; do

    echo "start copying chr${i}_v3.sample"

    if [ ${i} != "X" ] 
    then
        cp /n/groups/patel/uk_biobank/project_52887_genetics/ukb52887_imp_chr${i}_v3_s487296.sample /n/scratch3/users/t/tad368/samples/chr${i}_v3.sample
    else
        cp /n/groups/patel/uk_biobank/project_52887_genetics/ukb52887_imp_chrX_v3_s486645.sample /n/scratch3/users/t/tad368/samples/chrX_v3.sample
    fi

    echo "finished copying chr${i}_v3.sample"
    echo ""

done
