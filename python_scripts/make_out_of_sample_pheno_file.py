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
    parser.add_argument('-c', '--columns', help='Columns to keep', required=True)
    parser.add_argument('-v', '--covariates', type = int, nargs='+', default = [], help='Covariates to keep', required=False)
    args = parser.parse_args()

    input_file = args.input # input file of in-sample individuals
    output_file = args.output # out of sample individuals
    pheno_file = args.pheno # phenotype file
    columns = args.columns # file of columns to keep
    covariates = args.covariates # list of covariates to keep

    in_sample_IDs = pd.read_csv(input_file, sep='\t', header=None).iloc[:,0].tolist()

    index = 0

    # these are the only data fields we will need for PheWAS
    data_fields = sorted(pd.read_csv(columns, header=None, index_col = False).iloc[:,0].tolist() + covariates)
    exact_col_names = []
    # open file to write the IIDs to
    with open(output_file, "w") as data_file:
        
        # can't read entire .tab file at once, very slow, so read it in chunk by chunk
        chunksize = 1000 # number or rows we see at a time
        with pd.read_csv(pheno_file, sep = '\t', chunksize=chunksize, low_memory=False) as reader:
            
            # for each chunk of data
            for chunk in reader:

                if index == 0:
                    # get the column names
                    col_names = chunk.columns.tolist()

                    # get the column names that are in the list of columns to keep
                    for field in data_fields:
                        field = "." + str(field) + "."
                        for col_name in col_names:
                            if field in col_name:
                                exact_col_names.append(col_name)
                
                    #ensure columns are unique
                    exact_col_names = ['f.eid'] + list(dict.fromkeys(exact_col_names))
                    print(exact_col_names)
                    exit()
                # we only need to keep the phenotypes we want to run the PheWAS on
                chunk = chunk[exact_col_names]

                data = chunk[~chunk['f.eid'].isin(in_sample_IDs)] # get the data for the chunk that is not in the in-sample individuals

                if index == 0:
                    data.to_csv(data_file, sep='\t', header=True, index=False)
                else:
                    data.to_csv(data_file, sep='\t', header=False, index=False, mode='a')

                print('chunk ' + str(index) + ' done')
                index += 1


if __name__ == '__main__':
    main()