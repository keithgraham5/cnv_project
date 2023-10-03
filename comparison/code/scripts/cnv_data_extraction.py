import pandas as pd

cnvkit_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/H28194-21.sorted.dedup.recalibrated.Tumor.call.cns"
cnvrobot_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/sample_SAMPLE001_F_SEGMENTS_C-2_PoN-F_SEGM-smart-0.65_segmentation.tsv"
snp_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/test_snp_output.txt"

# def extract_data_from_snp_source(snp_source):
#     # Read data from source and extract CNV calls 
#     # Return data in the format [("chr1", (start, end call)),....]
#     # Store list in list in source list "call_data", [("chr1", (start, end call)),....]

#     # Return data in the format [("chr1", (start, end call)),....]
#     # Store list in list in source list "call_data", [("chr1", (start, end call)),....]


def extract_data_from_cnvkit_source(cnvkit_data):
    # Read the data into a pandas DataFrame
    df = pd.read_csv(cnvkit_data, delimiter="\t")

    # Filter rows where 'cn' is below or above 2
    filtered_df = df[(df['cn'] < 2) | (df['cn'] > 2)]

    # Initialise a list to store the formatted data
    formatted_data = []

    for index, row in filtered_df.iterrows():
        # Extract the relevant information from the DataFrame row
        chromosome = row['chromosome']
        start = row['start']
        end = row['end']
        log2 = row['log2']

        # Create a tuple with the extracted information
        data_tuple = (chromosome, (start, end, log2))

        # Append the data tuple to the formatted_data list
        formatted_data.append(data_tuple)

    return formatted_data

# Call the function with your file path
# filtered_cnvkit_data = extract_data_from_cnvkit_source(cnvkit_data)

# Create the output in the desired format
# output = ("cnvkit_data", filtered_cnvkit_data)

# Print the formatted output
# print(output)
    
def extract_data_from_cnvrobot_source(cnvrobot_data):
    # Read the data into a pandas DataFrame
    df = pd.read_csv(cnvrobot_data, delimiter="\t")
    
    # print("Column Header:")
    # print(df.columns.tolist())
    
   # Filter rows where 'TYPE' is either 'LOSS' or 'GAIN'
    filtered_df = df[df['TYPE'].isin(['LOSS', 'GAIN'])]
    
    # Intitalise a list to store the formated data
    formatted_data = []
    
    for index, row in filtered_df.iterrows():
        # print(filtered_df)
        
        #Extract the relevant information from the DataFrame row
        chromosome = row['CONTIG']
        print(chromosome)
        start = row['START']
        end = row['END']
        log2 = row['MEAN_L2R']

        # Create a tuple with the extracted information from the Dataframe row
        data_tuple = (chromosome, (start, end, log2))
        
        # Append the data tuple to the formatted_data list
        formatted_data.append(data_tuple)

    return formatted_data

# Call the function with the path to your CNVRobot data file
filtered_cnvrobot_data = extract_data_from_cnvrobot_source(cnvrobot_data)

# Create the output in the desired format 
output = ("cnvrobot_data", filtered_cnvrobot_data)

# Print formated output
print(output)


#     # Filter rows where 'cn' is below or above 2
#     filtered_df = df[(df['cn'] < 2) | (df['cn'] > 2)]

#     # Initialize a list to store the formatted data
#     formatted_data = []

#     for index, row in filtered_df.iterrows():
#         # Extract the relevant information from the DataFrame row
#         chromosome = row['chromosome']
#         start = row['start']
#         end = row['end']
#         log2 = row['log2']

#         # Create a tuple with the extracted information
#         data_tuple = (chromosome, (start, end, log2))

#         # Append the data tuple to the formatted_data list
#         formatted_data.append(data_tuple)

#     return formatted_data

# # Call the function with your file path
# filtered_cnvkit_data = extract_data_from_cnvkit_source(cnvkit_data)

# Create the output in the desired format
# #  extract data from each source 
# snp_data = extract_data_from_snp_source()
# cnvkit_source = extract_data_from_cnvkit_source()
# cnvrobot_source = extract_data_from_cnvrobot_source()

# Organise data into the desired format
data_sources = [
    (
        "call_data",
        [
            ("chr1", (200000, 149000000, -0.2)),
            # Add data for other chromosomes if needed
        ],
    ),
    (
        "cnvkit_data",
        [
            ("chr1", (1, 249250621, 0.1)),
            # Add data for other chromosomes if needed
        ],
    ),
    (
        "cnvrobot_data",
        [
            # ("chr1", (1, 249250621, 0.05)),
            # Add data for other chromosomes if needed
        ],
    ),
]