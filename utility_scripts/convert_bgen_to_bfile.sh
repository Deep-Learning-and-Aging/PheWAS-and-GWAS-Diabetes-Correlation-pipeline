#!/bin/bash
#SBATCH -c 8                                # Request one core
#SBATCH -t 0-24:00:00                       # Runtime in D-HH:MM format
#SBATCH -p medium                           # Partition to run in
#SBATCH --mem=128000M                        # Memory total in MiB (for all cores)
#SBATCH -o tad368_%j.out                    # File to which STDOUT will be written, including job ID (%j)
#SBATCH -e tad368_%j.err                    # File to which STDERR will be written, including job ID (%j)

module load plink2

plink2  --bgen /home/tad368/data_dir/geno/chr$1_v3.bgen \
            --sample /home/tad368/data_dir/samples/chr$1_v3.sample \
            --threads 16 \
            --memory 128000 \
            --make-bed \
            --out /home/tad368/data_dir/bfiles/chr$1_v3_bfile