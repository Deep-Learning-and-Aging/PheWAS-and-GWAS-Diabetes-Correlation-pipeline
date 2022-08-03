import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Create instruments for MR')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-t', '--text', help='Output file', required=True)

    args = parser.parse_args()
    input_file = args.input
    text_file = args.text

    keepinput = ['rsID', 'chr', 'pos', 'p']
    keeptext = ['rsID', 'chr', 'pos', 'non_effect_allele', 'effect_allele', 'se', 'beta']

    # read in the input file
    df = pd.read_csv(input_file, sep ='\t', usecols = keepinput)

    # read in the text file
    text_df = pd.read_csv(text_file, sep ='\t', usecols = keeptext)

    merged = pd.merge(df, text_df, on = ['rsID', 'chr', 'pos'])

    merged = merged[['rsID', 'chr', 'pos', 'non_effect_allele', 'effect_allele', 'beta', 'se', 'p']]

    merged.columns = ['rsID', 'CHR', 'POS', 'Non_effect', 'Effect', 'BETA', 'SE', 'P']

    print(merged.head())

    merged.to_csv(input_file, sep = '\t', index = False)


if __name__ == "__main__":
    main()