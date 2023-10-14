import pandas as pd
import io
import gzip



# Define column headers for the SNP_data file
# PROBE ID        AMPCH1  AMPCH2  PROCESSED LOG R RATIO   B ALLELE FREQUENCY
# LOG R PRODUCT   LOG R RATIO     GENOTYPE        CHROMOSOME      POSITION
# COPY #  TYPE    CYTO LOCN       GC CONTENT


# Define column headers for the cnvrobot data
# SEGMENTATION_CONDITION  PON_SEX_N       SAMPLE_ID1      SAMPLE_ID2
# SAMPLE_TYPE     SAMPLE_SEX      CONTIG  START   END
# MEAN_L2R        MEAN_L2R_EDIT   SIZE    PROBES  FILTER  TYPE    CHRBAND


# Define column headers for the cnvkit data
# chromosome      start   end     gene    log2    cn      depth   p_ttest probes
# weight

#KNOWNGENE.TXT
# Define the knownGene.txt headers 
# Name        Chrom   Strand  TxStart     TxEnd       CDSStart    CDSEnd  
# ExonCount   ExonStarts  ExonEnds     OtherInfo
knowngene = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/reference_data/knownGene.txt.gz'

# Define the filepaths for the data
# snp_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/test_snp_output.txt"
# regions_of_interest_data = "~/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/reference_data/20220207_PanHaemOnc.bed"

# Define the filepaths for the test data
snp_data = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/H23531_22-206443730041_R01C01_fused.csv'
regions_of_interest_data = "~/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/20220207_PanHaemOnc.bed"


# Define the mapping for renaming CHROMOSOME values
chromosome_mapping = {
    'chrX': 'chr23',
    'chrY': 'chr24'
}


# def read_csv_from_probe_id(csv_file_path):
    
#     # Create a list with the desired column headers
#     column_headers = [
#         'PROBE ID', 'AMPCH1', 'AMPCH2', 'PROCESSED LOG R RATIO',
#         'B ALLELE FREQUENCY', 'LOG R PRODUCT', 'LOG R RATIO',
#         'GENOTYPE', 'CHROMOSOME', 'POSITION', 'COPY #', 'TYPE',
#         'CYTO LOCN', 'GC CONTENT'
#     ]

#     # Initialize a flag to indicate whether to start reading
#     start_reading = False

#     # Create an empty list to store the lines of data
#     data_lines = []

#     # Open the CSV file for reading with tab as the delimiter
#     with open(csv_file_path, 'r') as file:
#         for line in file:
#             if start_reading:
#                 # If the flag is set, add the line to the list of data lines
#                 data_lines.append(line.strip())
#             elif 'PROBE ID' in line:
#                 # If 'PROBE ID' is found, set the flag to True to start reading
#                 start_reading = True

#     # Convert the data lines into a DataFrame with the custom column headers
#     if data_lines:
#         data_str = '\n'.join(data_lines)
#         df = pd.read_csv(io.StringIO(data_str), delimiter='\t', names=column_headers, header=None)
#         return df
#     else:
#         print("No 'PROBE ID' data found in the CSV file.")
#         return None

# # Example usage:
# csv_file_path = snp_data
# df_snp_1 = read_csv_from_probe_id(csv_file_path)



# # Create a new 'NEW_CHROMOSOME' column by prefixing 'chr' to 'CHROMOSOME' values
# df_snp_1['NEW_CHROMOSOME'] = 'chr' + df_snp_1['CHROMOSOME'].astype(str)

# # Print the first row with headers
# first_row_with_headers = df_snp_1.iloc[0]
# print(first_row_with_headers)




def read_and_rename_regions_of_interest(regions_of_interest_data, chromosome_mapping):
    """
    Reads a CSV file, renames columns, and replaces 'CHROMOSOME' values based on a mapping.

    Args:
        regions_of_interest_data (str): The path to the CSV file.
        chromosome_mapping (dict): A dictionary for mapping 'CHROMOSOME' values.

    Returns:
        pd.DataFrame: The DataFrame with renamed columns and mapped 'CHROMOSOME' values.
    """
    # Read the PanHaemOnc.bed file
    regions_of_interest = pd.read_csv(regions_of_interest_data, delimiter="\t")

    # Define column names for regions of interest
    column_names = ['CHROMOSOME', 'START', 'END', 'GENE']

    # Rename the columns in regions_of_interest
    regions_of_interest.columns = column_names

    # Rename the 'CHROMOSOME' values based on the mapping
    regions_of_interest['CHROMOSOME'] = regions_of_interest['CHROMOSOME'].replace(chromosome_mapping)
    
    return regions_of_interest

ROIs = read_and_rename_regions_of_interest(regions_of_interest_data, chromosome_mapping)
# print(ROIs)

# # Read the snp_data file
# snp_data = pd.read_csv(snp_data, delimiter="\t")

# # Get the column headers for snp_data
# column_headers = snp_data.columns

# # Create a new 'NEW_CHROMOSOME' column by prefixing 'chr' to 'CHROMOSOME' values
# snp_data['NEW_CHROMOSOME'] = 'chr' + snp_data['CHROMOSOME'].astype(str)

# # Merge the DataFrames based on the 'NEW_CHROMOSOME' column
# merged_data = df_snp_1.merge(regions_of_interest, left_on='NEW_CHROMOSOME', right_on='CHROMOSOME')

# # Filter rows where 'POSITION' is within the 'START' and 'END' range
# filtered_data = merged_data[(merged_data['POSITION'] >= merged_data['START']) & (merged_data['POSITION'] <= merged_data['END'])]

# # Filter rows in filtered_data where 'TYPE' is not 'NO CHANGE'
# filtered_data_not_no_change = filtered_data[filtered_data['TYPE'] != 'NO CHANGE']

# # Print the filtered data without 'NO CHANGE' in the 'TYPE' column
# print(filtered_data_not_no_change)

# # Calculate the number of included and discarded probes
# included_probes = len(filtered_data)
# discarded_probes = len(snp_data) - included_probes

# # Print the results
# print(filtered_data)
# print(f"Probes included: {included_probes}")
# print(f"Probes discarded: {discarded_probes}")

# cnvkit_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/H28310-21.sorted.dedup.recalibrated.Tumor.call.cns"

# # cnvkit_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_datatest_H28194-21.sorted.dedup.recalibrated.Tumor.call.cns"

# # Read the file into a DataFrame
# df = pd.read_csv(cnvkit_data, delimiter="\t")

# # Now, 'df' contains the data from the file as a DataFrame   
# print(df.columns)


# num_rows = df.shape[0]
# print(f"Number of rows: {num_rows}")
        
