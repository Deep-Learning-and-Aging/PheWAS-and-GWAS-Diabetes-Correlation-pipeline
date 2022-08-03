import pandas as pd

def main():

    eye = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_EyesOCT.tab'
    eye_fundus = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_EyesFundus.tab'

    eye_ids = pd.read_csv(eye, sep="\t", usecols = ['IID'])
    eye_fundus_ids = pd.read_csv(eye_fundus, sep="\t", usecols = ['IID'])

    # write the ids to the in_pop_ids directory for each of the three tab files
    eye_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/EyesOCT_in_sample_pop_IDs.txt', index=False, header=False)
    eye_fundus_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/EyesFundus_in_sample_pop_IDs.txt', index=False, header=False)


if __name__ == "__main__":
    main()