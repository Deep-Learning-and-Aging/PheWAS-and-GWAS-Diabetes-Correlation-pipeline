#!/bin/bash
#SBATCH -c 10                                                                                        # Request 20 cores
#SBATCH -t 2-00:00                                                                               # Runtime in D-HH:MM format
#SBATCH -p medium                                                                                    # Partition to run in
#SBATCH --mem=64000M                                                                                # Memory total in MiB (for all cores)
#SBATCH -o /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/batch_logs/compress_bfiles_%j.out   # File to which STDOUT will be written, including job ID (%j)
#SBATCH -e /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/batch_logs/compress_bfiles_%j.err   # File to which STDERR will be written, including job ID (%j)
#SBATCH --mail-type=ALL                                                                           # Type of email notification- BEGIN,END,FAIL,ALL

zstd --rm ~/data_dir/bfiles/*.bed