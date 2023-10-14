import pandas as pd

cnvkit_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/H28194-21.sorted.dedup.recalibrated.Tumor.call.cns"
cnvrobot_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/sample_SAMPLE001_F_SEGMENTS_C-2_PoN-F_SEGM-smart-0.65_segmentation.tsv"
snp_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/test_snp_output.txt"

# def extract_data_from_snp_source(snp_source):
#     # Read the data into a pandas Dataframe 
#     df = pd.read_csv(snp_data, delimiter="\t")
    
#     # Filter rows where '
        

# extraction.py

def extract_data_from_cnvkit_source(cnvkit_data):
    # Read the data into a pandas DataFrame
    df = pd.read_csv(cnvkit_data, delimiter="\t")

    # Filter rows where 'cn' is below or above 2
    filtered_df = df[(df['cn'] < 2) | (df['cn'] > 2)]

    # Initialize a list to store the formatted data
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

def extract_data_from_cnvrobot_source(cnvrobot_data):
    # Read the data into a pandas DataFrame
    df = pd.read_csv(cnvrobot_data, delimiter="\t")

   # Filter rows where 'TYPE' is either 'LOSS' or 'GAIN'
    filtered_df = df[df['TYPE'].isin(['LOSS', 'GAIN'])]
    
    # Initialize a list to store the formatted data
    formatted_data = []
    
    for index, row in filtered_df.iterrows():
        # Extract the relevant information from the DataFrame row
        chromosome = row['CONTIG']
        start = row['START']
        end = row['END']
        log2 = row['MEAN_L2R']

        # Create a tuple with the extracted information from the DataFrame row
        data_tuple = (chromosome, (start, end, log2))
        
        # Append the data tuple to the formatted_data list
        formatted_data.append(data_tuple)

    return formatted_data

def extract_data():
    # Paths to your data sources
    cnvkit_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/H28194-21.sorted.dedup.recalibrated.Tumor.call.cns"
    cnvrobot_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/sample_SAMPLE001_F_SEGMENTS_C-2_PoN-F_SEGM-smart-0.65_segmentation.tsv"
    snp_data = "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/comparison/data/test_data/test_snp_output.txt"


    # Call the extraction functions for each data source
    filtered_cnvkit_data = extract_data_from_cnvkit_source(cnvkit_data)
    filtered_cnvrobot_data = extract_data_from_cnvrobot_source(cnvrobot_data)
    
    # Create the output in the desired format
    cnvkit_output = ("cnvkit_data", filtered_cnvkit_data)
    cnvrobot_output = ("cnvrobot_data", filtered_cnvrobot_data)
    
    # Create a list to append both cnvkit_output and cnvrobot_output
    filtered_parsed_data = [cnvkit_output, cnvrobot_output]
    
    return filtered_parsed_data

if __name__ == "__main__":
    filtered_parsed_data = extract_data()







