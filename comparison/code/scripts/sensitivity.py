import pandas as pd


# Define the filepaths for the data
# snp_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/test_snp_output.txt"
# regions_of_interest_data = "~/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/reference_data/20220207_PanHaemOnc.bed"

# Define the filepaths for the test data
snp_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/shorter_test_snp_output.txt"
regions_of_interest_data = "~/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/shorter_20220207_PanHaemOnc.bed"


# Define the mapping for renaming CHROMOSOME values
chromosome_mapping = {
    'chrX': 'chr23',
    'chrY': 'chr24'
}

# Read the PanHaemOnc.bed file
regions_of_interest = pd.read_csv(regions_of_interest_data, delimiter="\t")

# Define column names for regions of interest
column_names = ['CHROMOSOME', 'START', 'END', 'GENE']

# Rename the columns in regions_of_interest
regions_of_interest.columns = column_names

# Rename the 'CHROMOSOME' values based on the mapping
regions_of_interest['CHROMOSOME'] = regions_of_interest['CHROMOSOME'].replace(chromosome_mapping)


# Read the snp_data file
snp_data = pd.read_csv(snp_data, delimiter="\t")

# Get the column headers for snp_data
column_headers = snp_data.columns

# Create a new 'NEW_CHROMOSOME' column by prefixing 'chr' to 'CHROMOSOME' values
snp_data['NEW_CHROMOSOME'] = 'chr' + snp_data['CHROMOSOME'].astype(str)

# Merge the DataFrames based on the 'NEW_CHROMOSOME' column
merged_data = snp_data.merge(regions_of_interest, left_on='NEW_CHROMOSOME', right_on='CHROMOSOME')

# Filter rows where 'POSITION' is within the 'START' and 'END' range
filtered_data = merged_data[(merged_data['POSITION'] >= merged_data['START']) & (merged_data['POSITION'] <= merged_data['END'])]

# Filter rows in filtered_data where 'TYPE' is not 'NO CHANGE'
filtered_data_not_no_change = filtered_data[filtered_data['TYPE'] != 'NO CHANGE']

# Print the filtered data without 'NO CHANGE' in the 'TYPE' column
print(filtered_data_not_no_change)

# Calculate the number of included and discarded probes
included_probes = len(filtered_data)
discarded_probes = len(snp_data) - included_probes

# Print the results
print(filtered_data)
print(f"Probes included: {included_probes}")
print(f"Probes discarded: {discarded_probes}")

cnvkit_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/H28310-21.sorted.dedup.recalibrated.Tumor.call.cns"

# cnvkit_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_datatest_H28194-21.sorted.dedup.recalibrated.Tumor.call.cns"

# Read the file into a DataFrame
df = pd.read_csv(cnvkit_data, delimiter="\t")

# Now, 'df' contains the data from the file as a DataFrame   
print(df.columns)


num_rows = df.shape[0]
print(f"Number of rows: {num_rows}")
        