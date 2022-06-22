import pandas as pd
import os
import argparse
import numpy as np

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Extract the individuals who had an MRI')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    args = parser.parse_args()

    input_file = args.input # phenotype tab file
    output_file = args.output # out of sample individuals

    # get path of output file
    output_path = os.path.dirname(output_file)
    data_file = output_path + '/out_of_sample_data.tab'

    # Read fields file
    fields = pd.read_csv("fields.txt").values.flatten()

    index = 0

    # open file to write the IIDs to
    with open(output_file, "w") as ID_file:
        # can't read entire .tab file at once, very slow, so read it in chunk by chunk
        chunksize = 1000 # number or rows we see at a time
        with pd.read_csv(input_file, sep = '\t', chunksize=chunksize, low_memory=False) as reader:
            
            # for each chunk of data
            for chunk in reader:
                if(index != 0):
                    ID_file.write("\n")

                # drop the rows that have missing values for every field from the fields file
                data_subset = chunk[fields].dropna(axis=0, how='all')

                # get the indices of the out-of-sample pop by taking reverse of in-sample
                out_sample_pop = chunk.index.difference(data_subset.index)

                # grab the the rows that have a value for every field from the fields file along with all their phenotype data
                full_data = chunk.loc[out_sample_pop]

                if(index == 0):
                    full_data.to_csv(data_file, sep='\t', index=False)
                else:
                    full_data.to_csv(data_file, sep='\t', index=False, header=False, mode='a')
                
                # using the indices of the rows that have no missing values, get the IIDs
                IIDs = chunk.loc[data_subset.index]['f.eid'].values.tolist()

                # write the IIDs to the output file
                ID_file.write('\n'.join(str(id) + '\t' + str(id) for id in IIDs))

                print('chunk ' + str(index) + ' done')
                index += 1

                # we essentially just retain the in-sample-population IIDs, which we will
                # then remove from the full population, to get the out-of-sample-population IIDs

if __name__ == '__main__':
    main()