#!/bin/bash
#SBATCH -c 4                                                                                        # Request one core
#SBATCH -t 0-00:30:00                                                                                # Runtime in D-HH:MM format
#SBATCH -p short                                                                                    # Partition to run in
#SBATCH --mem=64000M                                                                                # Memory total in MiB (for all cores)
#SBATCH -o /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/batch_logs/extract_%j.out   # File to which STDOUT will be written, including job ID (%j)
#SBATCH -e /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/batch_logs/extract_%j.err   # File to which STDERR will be written, including job ID (%j)


module load plink2
python3 /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/python_scripts/extract.py \
        -i /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/variants_list/AbdAge_Top_SNPS.tsv \
        -d /home/tad368/data_dir/ \
        -r /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/pop_IDs/Abdomen_in_sample_pop_IDs.txt

python3 /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/python_scripts/extract.py \
        -i /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/variants_list/LivAge_Top_SNPS.tsv \
        -d /home/tad368/data_dir/ \
        -r /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/pop_IDs/Liver_in_sample_pop_IDs.txt

python3 /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/python_scripts/extract.py \
        -i /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/variants_list/PancAge_Top_SNPS.tsv \
        -d /home/tad368/data_dir/ \
        -r /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/pop_IDs/Pancreas_in_sample_pop_IDs.txt