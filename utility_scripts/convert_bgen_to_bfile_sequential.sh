#!/bin/bash
#SBATCH -c 8                                # Request one core
#SBATCH -t 0-48:00:00                       # Runtime in D-HH:MM format
#SBATCH -p medium                           # Partition to run in
#SBATCH --mem=128000M                        # Memory total in MiB (for all cores)
#SBATCH -o tad368_%j.out                    # File to which STDOUT will be written, including job ID (%j)
#SBATCH -e tad368_%j.err                    # File to which STDERR will be written, including job ID (%j)
#SBATCH --mail-type=ALL                                                                           # Type of email notification- BEGIN,END,FAIL,ALL

list=()

for i in {1..22}; do
    list+=($i)
done

list+=(X)
# list+=(XY) --> does exist for bgen files but no sample file available
# list+=(Y) --> doesn't exist for bgen files

module load plink2

for i in "${list[@]}"; do

    echo "started creating chr${i}_v3_bfile"

    plink2  --bgen /home/tad368/data_dir/geno/chr${i}_v3.bgen \
            --sample /home/tad368/data_dir/samples/chr${i}_v3.sample \
            --threads 8 \
            --memory 32000 \
            --make-bed \
            --out /home/tad368/data_dir/bfiles/chr${i}_v3_bfile \

    echo "finished creating chr${i}_v3_bfile"
    echo ""

done