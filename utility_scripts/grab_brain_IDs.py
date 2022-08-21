import pandas as pd

def main():

    brain = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_Brain.tab'
    # brain_cog = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_BrainCognitive.tab'
    brain_mri = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_BrainMRI.tab'

    brain_ids = pd.read_csv(brain, sep="\t", usecols = ['IID'])
    # brain_cog_ids = pd.read_csv(brain_cog, sep="\t", usecols = ['IID'])
    brain_mri_ids = pd.read_csv(brain_mri, sep="\t", usecols = ['IID'])

    # write the ids to the in_pop_ids directory for each of the three tab files
    brain_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/Brain_in_sample_pop_IDs.txt', index=False, header=False)
    # brain_cog_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/BrainCognitive_in_sample_pop_IDs.txt', index=False, header=False)
    brain_mri_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/BrainMRI_in_sample_pop_IDs.txt', index=False, header=False)


if __name__ == "__main__":
    main()