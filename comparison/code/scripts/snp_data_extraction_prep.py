


import pandas as pd
import io
import sys

# Define the mapping for renaming CHROMOSOME values
chromosome_mapping = {
    'chrX': 'chr23',
    'chrY': 'chr24'
}


def read_csv_from_probe_id(csv_file_path):
    """
    Reads a CSV file, extracts data starting from the 'PROBE ID' section, and returns a DataFrame.

    Args:
        csv_file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame or None: A DataFrame containing the extracted data with custom column headers.
                             Returns None if 'PROBE ID' data is not found in the CSV file.
    """
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


def add_new_chromosome_column(df):
    """
    Adds a new 'NEW_CHROMOSOME' column to the DataFrame by prefixing 'chr' to 'CHROMOSOME' values.

    Args:
        df (pd.DataFrame): The DataFrame to which the column will be added.

    Returns:
        pd.DataFrame: The DataFrame with the 'NEW_CHROMOSOME' column added.
    """
    # Create the 'NEW_CHROMOSOME' column by prefixing 'chr' to 'CHROMOSOME' values
    df['NEW_CHROMOSOME'] = 'chr' + df['CHROMOSOME'].astype(str)
    
    return df

def drop_columns(df):
        # Drop one or more columns by name
    columns_to_drop = [
        'AMPCH1', 'AMPCH2', 'PROCESSED LOG R RATIO',
        'B ALLELE FREQUENCY', 'LOG R PRODUCT', 'LOG R RATIO',
        'GENOTYPE', 'CHROMOSOME', 'COPY #', 'TYPE',
        'CYTO LOCN', 'GC CONTENT'
    ]
    df = df.drop(columns=columns_to_drop)
    return df
        

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


# def capture_probes_in_regions_of_interest(df_rois, df_snp_1):
#     filtered_rows = []
#     discarded_count = 0
#     kept_count = 0

#     for index_a, row_a in df_rois.iterrows():
#         chromosome_a, start, end = row_a['CHROMOSOME'], row_a['START'], row_a['END']
        
#         for index_b, row_b in df_snp_1.iterrows():
#             chromosome_b, position = row_b['NEW_CHROMOSOME'], row_b['POSITION']
            
#             if chromosome_a == chromosome_b and start <= position <= end:
#                 filtered_rows.append(row_b)
#                 kept_count += 1
#             else:
#                 discarded_count += 1

#     filtered_df = pd.DataFrame(filtered_rows)

#     print(filtered_df)
#     print(f"Probes Kept: {kept_count}")
#     print(f"Probes Discarded: {discarded_count}")





    

    



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <snp_csv_file_path> <regions_of_interest_file_path>")
        sys.exit(1)

    snp_csv_file_path = sys.argv[1]
    regions_of_interest_file_path = sys.argv[2]
    
    df_snp_1 = read_csv_from_probe_id(snp_csv_file_path)
    df_snp_1 = add_new_chromosome_column(df_snp_1)
    df_rois = read_and_rename_regions_of_interest(regions_of_interest_file_path, chromosome_mapping)
    df_snp_id = drop_columns(df_snp_1)
    df_snp_id.to_csv('~/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/df_snp_id.csv', header=0, index=False)
sqlite
    # capture_probes_in_regions_of_interest(df_rois, df_snp_1)

   
