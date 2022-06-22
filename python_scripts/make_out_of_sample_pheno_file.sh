#!/bin/bash
#SBATCH -c 4                                # Request one core
#SBATCH -t 0-2:00:00                       # Runtime in D-HH:MM format
#SBATCH -p short                           # Partition to run in
#SBATCH --mem=64000M                        # Memory total in MiB (for all cores)
#SBATCH -o grabIds_%j.out                    # File to which STDOUT will be written, including job ID (%j)
#SBATCH -e grabIds_%j.err                    # File to which STDERR will be written, including job ID (%j)

python3 ./make_out_of_sample_pheno_file.py -i $1 -o $2