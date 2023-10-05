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


    


    
    # unique_values = df['NEW_CHROMOSOME'].unique()
    # print(unique_values)
    # Use loc to filter rows where CHROMOSOME is '25' and print the first row
    # Check if there are any rows with CHROMOSOME equal to '25'
    
    # if 25 in df['CHROMOSOME'].values:
    #     # If there are, find and print the first row
    #     first_row_with_25 = df.loc[df['CHROMOSOME'] == 25].iloc[0]
    #     print(first_row_with_25)
    # else:
    #     print("No rows with CHROMOSOME equal to '25'")
        
    # count_25 = (df['CHROMOSOME'] == 25).sum()
    # print(f"Count of '25' in CHROMOSOME column: {count_25}")
    
    

    # # Filter rows where 'cn' is below or above 2
    # filtered_df = df[(df['cn'] < 2) | (df['cn'] > 2)]

    # # Initialize a list to store the formatted data
    # formatted_data = []

    # for index, row in filtered_df.iterrows():
    #     # Extract the relevant information from the DataFrame row
    #     chromosome = row['chromosome']
    #     start = row['start']
    #     end = row['end']
    #     log2 = row['log2']

    #     # Create a tuple with the extracted information
    #     data_tuple = (chromosome, (start, end, log2))

    #     # Append the data tuple to the formatted_data list
    #     formatted_data.append(data_tuple)

    # return formatted_data

# extract_data_from_snp_data(snp_data)