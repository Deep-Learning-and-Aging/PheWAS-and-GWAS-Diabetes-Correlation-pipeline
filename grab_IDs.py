import pandas as pd
import os
import argparse
import numpy as np

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Extract the individuals who had a Liver MRI')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    # Read fields file
    fields = pd.read_csv("fields.txt").values.flatten()

    index = 0

    # open file to write the IIDs to
    with open(output_file, "w") as outfile:

        # can't read entire .tab file at once, very slow, so read it in chunk by chunk
        chunksize = 1000 # number or rows we see at a time
        with pd.read_csv(input_file, sep = '\t', chunksize=chunksize, low_memory=False) as reader:
            
            # for each chunk of data
            for chunk in reader:
                print('chunk ' + str(index) + ' done')
                index += 1

                # drop the rows that have missing values for every field from the fields file
                data = chunk[fields].dropna(axis=0, how='all')

                # using the indices of the rows that have no missing values, get the IIDs
                IIDs = chunk.loc[data.index]['f.eid'].values.tolist()

                # write the IIDs to the output file
                outfile.write('\n'.join(str(id) for id in IIDs))

                # we essentially just retain the in-sample-population IIDs, which we will
                # then remove from the full population, to get the out-of-sample-population IIDs

if __name__ == '__main__':
    main()

