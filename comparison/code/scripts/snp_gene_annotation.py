import pandas as pd
import io

# Define column headers for the SNP_data file
# PROBE ID        AMPCH1  AMPCH2  PROCESSED LOG R RATIO   B ALLELE FREQUENCY
# LOG R PRODUCT   LOG R RATIO     GENOTYPE        CHROMOSOME      POSITION
# COPY #  TYPE    CYTO LOCN       GC CONTENT
snp_1 = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/H23531_22-206443730041_R01C01_fused.csv'
snp_2 = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/H30296_21-205805560092_R06C01_fused.csv'

#KNOWNGENE.TXT
# Define the knownGene.txt headers 
# Name        Chrom   Strand  TxStart     TxEnd       CDSStart    CDSEnd  
# ExonCount   ExonStarts  ExonEnds     OtherInfo
knowngene = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/knownGene.txt.gz'

omimgene = '/home/keith/reference_data/Omimgenemap2.txt'
# Chromosome    Genomic Position Start  Genomic Position End    Cyto Location   
# Computed Cyto Location  Mim Number      Gene Symbols    Gene Name       
# Approved Symbol Entrez Gene ID  Ensembl Gene ID Comments  
# Phenotypes      Mouse Gene Symbol/ID



# # Read the csv file
# df_snp_1 = pd.read_csv(snp_1)


import pandas as pd
import io

def read_csv_from_probe_id(csv_file_path):
    # Create a list with the desired column headers
    column_headers = [
        'PROBE ID', 'AMPCH1', 'AMPCH2', 'PROCESSED LOG R RATIO',
        'B ALLELE FREQUENCY', 'LOG R PRODUCT', 'LOG R RATIO',
        'GENOTYPE', 'CHROMOSOME', 'POSITION', 'COPY #', 'TYPE',
        'CYTO LOCN', 'GC CONTENT'
    ]

    # Initialize a flag to indicate whether to start reading
    start_reading = False

    # Create an empty list to store the lines of data
    data_lines = []

    # Open the CSV file for reading with tab as the delimiter
    with open(csv_file_path, 'r') as file:
        for line in file:
            if start_reading:
                # If the flag is set, add the line to the list of data lines
                data_lines.append(line.strip())
            elif 'PROBE ID' in line:
                # If 'PROBE ID' is found, set the flag to True to start reading
                start_reading = True

    # Convert the data lines into a DataFrame with the custom column headers
    if data_lines:
        data_str = '\n'.join(data_lines)
        df = pd.read_csv(io.StringIO(data_str), delimiter='\t', names=column_headers, header=None)
        return df
    else:
        print("No 'PROBE ID' data found in the CSV file.")
        return None

# Example usage:
csv_file_path = snp_1
df_snp_1 = read_csv_from_probe_id(csv_file_path)



# Create a new 'NEW_CHROMOSOME' column by prefixing 'chr' to 'CHROMOSOME' values
df_snp_1['NEW_CHROMOSOME'] = 'chr' + df_snp_1['CHROMOSOME'].astype(str)

# Print the first row with headers
first_row_with_headers = df_snp_1.iloc[0]
print(first_row_with_headers)


import pandas as pd
import io

# def read_csv_from_probe_id_skip_until_chromosome_custom_headers(csv_file_path):
#     # Create a list with the desired column headers
#     column_headers = [
#         'Chromosome', 'Genomic Position Start', 'Genomic Position End',
#         'Cyto Location', 'Computed Cyto Location', 'Mim Number',
#         'Gene Symbols', 'Gene Name', 'Approved Symbol',
#         'Entrez Gene ID', 'Ensembl Gene ID', 'Comments',
#         'Phenotypes', 'Mouse Gene Symbol/ID'
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
#             elif line.strip().startswith('# Chromosome'):
#                 # If a line starts with '# Chromosome', set the flag to True to start reading
#                 start_reading = True

#     # Convert the data lines into a DataFrame with the custom column headers
#     if data_lines:
#         data_str = '\n'.join(data_lines)
#         df = pd.read_csv(io.StringIO(data_str), delimiter='\t', names=column_headers, header=None)
#         return df
#     else:
#         print("No '# Chromosome' data found in the CSV file.")
#         return None

# # Example usage:
# csv_file_path = omimgene
# df_snp_1_custom_headers = read_csv_from_probe_id_skip_until_chromosome_custom_headers(csv_file_path)

# # Print the first row with headers
# first_row_with_custom_headers = df_snp_1_custom_headers.iloc[0]
# print(first_row_with_custom_headers)




import pandas as pd
import gzip

# Specify the path to your compressed data file
compressed_data_file_path = knowngene

# Read the compressed data file into a list of lines
lines = []

# Open the compressed file and decompress while reading
with gzip.open(compressed_data_file_path, 'rt') as file:
    for line in file:
        lines.append(line)

# Define the column headers
column_headers = [
    'Name', 'Chrom', 'Strand', 'TxStart', 'TxEnd',
    'CDSStart', 'CDSEnd', 'ExonCount', 'ExonStarts',
    'ExonEnds', 'OtherInfo', 'OtherOtherInfo'
]

# Process each line and split it into columns
data = []
for line in lines:
    parts = line.strip().split('\t')
    # Join extra fields after 'ExonEnds' into 'OtherInfo'
    if len(parts) > len(column_headers):
        extra_info = '\t'.join(parts[len(column_headers):])
        parts = parts[:len(column_headers)] + [extra_info]
    data.append(parts)

# Create a DataFrame from the processed data
df = pd.DataFrame(data, columns=column_headers)

# Print the DataFrame
# print(df)
# Print the first row with headers
first_row_with_headers = df.iloc[2]
print(first_row_with_heade