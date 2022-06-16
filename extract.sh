#SBATCH -c 4                               # Request one core
#SBATCH -t 0-12:00:00                         # Runtime in D-HH:MM format
#SBATCH -p short                           # Partition to run in
#SBATCH --mem=64000M                         # Memory total in MiB (for all cores)
#SBATCH -o tad368_%j.out                 # File to which STDOUT will be written, including job ID (%j)
#SBATCH -e tad368_%j.err                 # File to which STDERR will be written, including job ID (%j)

module load plink2

python3 /home/tad368/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/extract.py $1 -i $2 -d