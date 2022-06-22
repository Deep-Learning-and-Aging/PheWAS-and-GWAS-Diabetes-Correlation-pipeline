#!/bin/bash
#SBATCH -c 4                                # Request one core
#SBATCH -t 0-2:00:00                       # Runtime in D-HH:MM format
#SBATCH -p short                           # Partition to run in
#SBATCH --mem=64000M                        # Memory total in MiB (for all cores)
#SBATCH -o grabIds_%j.out                    # File to which STDOUT will be written, including job ID (%j)
#SBATCH -e grabIds_%j.err                    # File to which STDERR will be written, including job ID (%j)

python3 ./make_out_of_sample_pheno_file.py -i /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/Abdomen_in_sample_pop_IDs.txt \
-o /home/tad368/data_dir/pheno/out_of_sample.tab \
-p /home/tad368/data_dir/pheno/pheno.tab \
-c /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/data_fields/lab_measures.txt