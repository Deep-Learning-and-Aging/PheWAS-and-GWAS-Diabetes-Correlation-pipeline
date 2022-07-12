import pandas as pd

def main():
    abdomen = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_Abdomen.tab'
    liver = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_AbdomenLiver.tab'
    pancreas = '/n/groups/patel/Alan/Aging/Medical_Images/data/GWAS_data_Age_AbdomenPancreas.tab'

    abdomen_ids = pd.read_csv(abdomen, sep="\t", usecols = ['IID'])
    liver_ids = pd.read_csv(liver, sep="\t", usecols = ['IID'])
    pancreas_ids = pd.read_csv(pancreas, sep="\t", usecols = ['IID'])

    # write the ids to the in_pop_ids directory for each of the three tab files
    abdomen_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/Abdomen_in_sample_pop_IDs.txt', index=False, header=False)
    liver_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/Liver_in_sample_pop_IDs.txt', index=False, header=False)
    pancreas_ids.to_csv('~/PheWAS-and-GWAS-Diabetes-Correlation-pipeline/in_pop_IDs/Pancreas_in_sample_pop_IDs.txt', index=False, header=False)


if __name__ == "__main__":
    main()