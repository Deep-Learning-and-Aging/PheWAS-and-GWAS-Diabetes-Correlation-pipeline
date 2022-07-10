#!/bin/bash
#SBATCH -c 4                                                                                        # Request one core
#SBATCH -t 0-4:00:00                                                                               # Runtime in D-HH:MM format
#SBATCH -p short                                                                                    # Partition to run in
#SBATCH --mem=128000M                                                                                # Memory total in MiB (for all cores)
#SBATCH -o /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/batch_logs/run_batch_Phewas%j.out   # File to which STDOUT will be written, including job ID (%j)
#SBATCH -e /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/batch_logs/run_batch_Phewas%j.err   # File to which STDERR will be written, including job ID (%j)

# grab just the file name (assuming no periods in file name) remove duplicates, and store in array (bfiles)
mapfile -t bfiles < <( find ~/data_dir/out/ -type f -print | awk -F'[/.]' '{print $(NF-1)}' | sort -u )

# create raw files using 0/1/2 encoding and then run PheWAS code (https://www.cog-genomics.org/plink/2.0/data#export)
for i in "${bfiles[@]}"; do
    python3 ~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/python_scripts/run_PheWAS.py \
                                --phenotype ~/data_dir/pheno/OOS_cov_fixed.tab \
                                --genotype ~/data_dir/raw_files/${i}.raw \
                                --covariates ~/data_dir/pheno/covariates.txt \
                                --out ~/data_dir/pheWAS_results/${i}_PHEWAS_RESULTS.tsv

done

