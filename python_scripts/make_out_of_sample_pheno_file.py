import pandas as pd
import os
import argparse
import numpy as np

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Extract the individuals who had an MRI')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-p', '--pheno', help='Phenotype file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    args = parser.parse_args()

    input_file = args.input # input file of in-sample individuals
    output_file = args.output # out of sample individuals
    pheno_file = args.pheno # phenotype file

    in_sample_IDs = pd.read_csv(input_file, sep='\t', header=None).iloc[:,0].tolist()

    index = 0

    # open file to write the IIDs to
    with open(output_file, "w") as data_file:
        
        # can't read entire .tab file at once, very slow, so read it in chunk by chunk
        chunksize = 1000 # number or rows we see at a time
        with pd.read_csv(pheno_file, sep = '\t', chunksize=chunksize, low_memory=False) as reader:
            
            # for each chunk of data
            for chunk in reader:

                data = chunk[~chunk['f.eid'].isin(in_sample_IDs)] # get the data for the chunk that is not in the in-sample individuals
                
                if index == 0:
                    data.to_csv(data_file, sep='\t', header=True, index=False)
                else:
                    data.to_csv(data_file, sep='\t', header=False, index=False, mode='a')

                print('chunk ' + str(index) + ' done')
                index += 1


if __name__ == '__main__':
    main()