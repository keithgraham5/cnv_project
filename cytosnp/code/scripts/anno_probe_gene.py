import pandas as pd
import io

input_cytosnp_file_path = (
    "/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/"
    "cnv_project/cytosnp/data/processed_data/intermediate/"
    "headless_H23531_22-206443730041_R01C01_fused.txt"
)
output_cytosnp_file_path = (
    '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/'
    'cnv_project/comparison/data/test_data/'
    'annotated_headless_H23531_22-206443730041_R01C01_fused.txt'
)
interval_file_path = (
    '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/'
    'cnv_project/cytosnp/data/reference_data/'
    'cyto_loc_20220207_PanHaemOnc.bed'
)
chromosome_mapping = {
    'chr1': 1,
    'chr2': 2,
    'chr3': 3,
    'chr4': 4,
    'chr5': 5,
    'chr6': 6,
    'chr7': 7,
    'chr8': 8,
    'chr9': 9,
    'chr10': 10,
    'chr11': 11,
    'chr12': 12,
    'chr13': 13,
    'chr14': 14,
    'chr15': 15,
    'chr16': 16,
    'chr17': 17,
    'chr18': 18,
    'chr19': 19,
    'chr20': 20,
    'chr21': 21,
    'chr22': 22,
    'chrX': 23,
    'chrY': 24
}


def annotate_snp_with_interval(interval_file_path, cytosnp_file_path, 
                               output_cytosnp_file_path):
    # Read the interval list
        # Read the interval list
    interval_list_df = (
        pd.read_csv(
            interval_file_path,
            sep='\t',
            header=None,
            names=['Chromosome', 'Start', 'End', 'GeneName', 
                   'CytogeneticLocations']
        )
    )
    # print(interval_file_path)
    # print(input_cytosnp_file_path)
    # Read the input SNP data
    cytosnp_df = pd.read_csv(input_cytosnp_file_path, delimiter='\t')
    

    # Create an empty list to store the updated probe data
    updated_probe_data = []

    # Ensure consistent data types for grouping columns
    interval_list_df['Chromosome'] = (interval_list_df
                                             ['Chromosome'].astype(str))
    interval_list_df['CytogeneticLocations'] = (interval_list_df
                                                       ['CytogeneticLocations']
                                                       .astype(str))
    print(cytosnp_df.columns)
    cytosnp_df['CHROMOSOME'] = cytosnp_df['CHROMOSOME'].astype(str)
#     cytosnp_df['CYTO LOCN'] = cytosnp_df['CYTO LOCN'].astype(str)

#     # Group intervals by chromosome and cytogenetic location
#     interval_chr_grouped = (interval_list_df
#                             .groupby['Chromosome', 'CytogeneticLocations'])
#     # Group probes by chromosome and cytogenetic location
#     probe_chr_grouped = cytosnp_df.groupby(['CHROMOSOME', 'CYTO LOCN'])

#     # Iterate through probes and match probes to intervals
#     for probe_index, probe_row in cytosnp_df.iterrows():
#         # Get the current probe's chromosome and cytogenetic location
#         probe_chromosome = probe_row['CHROMOSOME']
#         probe_cyto_location = probe_row['CYTO LOCN']

#         try:
#             # Get the group of intervals that match the current probe's 
#             # chromosome and cytogenetic location
#             matching_intervals = interval_chr_grouped.get_group
#             ((probe_chromosome, probe_cyto_location))

#             # Check if there's at least one matching interval
#             if not matching_intervals.empty:
#                 # Extract the GeneName from the first matching interval 
#                 gene_name = matching_intervals.iloc[0]['GeneName']

#                 # Update the probe data with the GeneName
#                 probe_row['GENE NAME'] = gene_name

#         except KeyError:
#             # Handle the case where there are no matching intervals for this 
#             # probe
#             pass

#         # Append the probe data (including GeneName, if found) to the 
#         # updated_probe_data list
#         updated_probe_data.append(probe_row)

#     # Create a new DataFrame with the updated probe data
#     updated_probe_df = pd.DataFrame(updated_probe_data)

#     # Save the updated DataFrame as a CSV file
#     updated_probe_df.to_csv(output_csv_file_path, sep='\t', index=False)

#     return updated_probe_df


# # Specify the path where you want to save the CSV file
# output_csv_file_path = '/path/to/output/file.csv'

annotate_snp_with_interval(interval_file_path, input_cytosnp_file_path, 
                           output_cytosnp_file_path)
