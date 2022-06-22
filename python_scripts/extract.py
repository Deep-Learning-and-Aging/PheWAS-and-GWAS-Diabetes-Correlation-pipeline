import os
import argparse
import pandas as pd
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Extract the data from the input file')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-d', '--directory', help='Directory', required=True)
    parser.add_argument('-r', '--remove', help='Output file', required=True)
    args = parser.parse_args()

    # Parse the command line arguments
    input_file = args.input
    data_directory = args.directory
    remove = args.remove

    # Determine the age predictor being used
    age_Predictor = input_file.split('/')[-1].split('.')[0].split('_')[0]

    # read the file of variants
    variants = pd.read_csv(input_file, sep='\t', header=0)
    chr = set(variants['CHR'].values)
    rsIDs = variants['rsID'].values

    temp_file = age_Predictor + '_temp_rsIDs_file.txt'

    with open(temp_file, 'w+') as f:
        f.write('\n'.join(rsIDs))

    for i in chr:
        subprocess.run(["plink2", "--bfile", data_directory + 'bfiles/chr'+ str(i) +'_v3_bfile', 
                        "--extract", temp_file, 
                        "--remove", remove,
                        "--threads", "8",
                        "--memory", "32000",
                        "--make-bed", 
                        "--out", data_directory + 'out/'+ age_Predictor +'_chr'+ str(i) +'_v3'])
        print('chr' + str(i) + ' done')

    os.remove(temp_file)
       

if __name__ == '__main__':
    main()