import pandas as pd 



snp_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/test_snp_output.txt"
regions_of_interesa_data = "~/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/reference_data/20220207_PanHaemOnc.bed"




df = pd.read_csv(snp_data, delimiter="\t")
column_headers = df.columns
df['NEW_CHROMOSOME'] = 'chr' +df['CHROMOSOME'].astype(str)
print(f" snp_data columns header:\n {column_headers}")
print(df.iloc[0])

column_names = ['CHROMOSOME', 'START', 'END', 'GENE']
df = pd.read_csv(regions_of_interesa_data, delimiter="\t")
df = pd.DataFrame(df)
df.columns = column_names
column_headers = df.columns 
print(f"PanHeamOnc.bed file columns header:\n {column_headers}")
print(df.iloc[0])

# Initialise an empty list to store filtered SNP data
# Loop through each row in the PanHaemOnc.bed file
# Filter SNP data based on matching 'NEW_CHROMOSOME'
# Filter SNP data further based on 'POSITION' within 'START' and 'END'
# Append filtered rows to the result
# Concatenate all the filtered SNP data rows into a single DataFrame
# Now, filtered_snp_data_df contains SNP data that falls within the regions of interest

