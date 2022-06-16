#!/bin/bash

list=()

for i in {1..22}; do
    list+=($i)
done

list+=(X)
list+=(Y)
list+=(XY)

for i in "${list[@]}"; do
    cp /n/groups/patel/uk_biobank/project_52887_genetics/ukb52887_cal_chr${i}_v2_s488264.fam /n/scratch3/users/t/tad368/geno/chr${i}_v2.fam

    echo "copied"

    echo "chr${i}_v2.fam"

    cp /n/groups/patel/uk_biobank/project_52887_genetics/ukb_cal_chr${i}_v2.bed /n/scratch3/users/t/tad368/geno/chr${i}_v2.bed

    echo "chr${i}_v2.bed"

    cp /n/groups/patel/uk_biobank/project_52887_genetics/ukb_snp_chr${i}_v2.bim /n/scratch3/users/t/tad368/geno/chr${i}_v2.bim

    echo "chr${i}_v2.bim"
    
    echo ""
done
