import pandas as pd

def main():
    heart = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_Heart.tab'
    heartmri = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_HeartMRI.tab'
    heartecg = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_HeartECG.tab'

    heart_ids = pd.read_csv(heart, sep="\t", usecols = ['IID'])
    heartmri_ids = pd.read_csv(heartmri, sep="\t", usecols = ['IID'])
    heartecg_ids = pd.read_csv(heartecg, sep="\t", usecols = ['IID'])

    # write the ids to the in_pop_ids directory for each of the three tab files
    heart_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/HeartScalar_in_sample_pop_IDs.txt', index=False, header=False)
    heartmri_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/HeartMRI_in_sample_pop_IDs.txt', index=False, header=False)
    heartecg_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/HeartECG_in_sample_pop_IDs.txt', index=False, header=False)


if __name__ == "__main__":
    main()