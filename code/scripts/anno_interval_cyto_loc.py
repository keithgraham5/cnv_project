import pandas as pd

def annotate_interval_file_with_cytolocation(interval_list_path, cyto_loc_file_path, output_file_path):
    
       """
    Annotate an interval file with cytogenetic location information and save the result as a CSV file.

    Parameters:
    - interval_list_path (str): Path to the interval list file containing chromosome, start, end, and gene name data.
    - cyto_loc_file_path (str): Path to the cytogenetic location file containing chromosome, start, end, region name, and band type data.
    - output_file_path (str): Path to save the annotated interval list as a CSV file.

    Returns:
    - None

    This function reads data from the interval list and cytogenetic location files, annotates the intervals
    with cytogenetic location information, and saves the result as a CSV file. It associates each interval with
    its corresponding cytogenetic locations and gene names.

    Usage example:
    annotate_interval_file_with_cytolocation("interval_list.txt", "cyto_loc.txt", "annotated_intervals.csv")
    """
    
    # Read the cytogenetic location data
    cyto_loc = pd.read_csv(cyto_loc_file_path, sep='\t', header=None, 
                           names=['Chromosome', 'Start', 'End', 'Region Name', 
                                  'Band Type'])
    cyto_loc['Chromosome'] = cyto_loc['Chromosome'].str.replace('chr', '')
    cyto_loc['Region Name'] = cyto_loc['Chromosome'] + cyto_loc['Region Name']  # Concatenate Chromosome and Region Name
    print(cyto_loc.iloc[0])
    
    # Read the interval list
    interval_list = pd.read_csv(interval_list_path, sep='\t', header=None, 
                                names=['Chromosome', 'Start', 'End', 'GeneName'])

    # Remove the "chr" prefix from the Chromosome column
    interval_list['Chromosome'] = interval_list['Chromosome'].str.replace('chr', '')
    
    # Initialize a dictionary to store cytogenetic locations and GeneNames for each unique region
    region_cyto_gene_locations = {}
    
    # Iterate through the cytogenetic location data and collect information
    for _, cyto_row in cyto_loc.iterrows():
        cyto_chromosome = cyto_row['Chromosome']
        cyto_start = cyto_row['Start']
        cyto_end = cyto_row['End']
        cyto_region_name = cyto_row['Region Name']
        
        # Iterate through the interval list and check for overlapping regions
        for _, interval_row in interval_list.iterrows():
            interval_chromosome = interval_row['Chromosome']
            interval_start = interval_row['Start']
            interval_end = interval_row['End']
            gene_name = interval_row['GeneName']
            
            
            if (cyto_chromosome == interval_chromosome and
                cyto_start <= interval_end and cyto_end >= interval_start):
                # Check if the region key is in the dictionary, and if not, initialize it
                region_key = (interval_chromosome, interval_start, interval_end, gene_name)
                if region_key not in region_cyto_gene_locations:
                    region_cyto_gene_locations[region_key] = {'CytogeneticLocations': [], 'GeneNames': []}
                    
                # Append the cytogenetic location and GeneName to the respective lists for this region
                region_cyto_gene_locations[region_key]['CytogeneticLocations'].append(cyto_region_name)
                region_cyto_gene_locations[region_key]['GeneNames'].append(gene_name)

    # Create a new DataFrame with columns for Chromosome, Start, End, GeneName, CytogeneticLocations
    result_data = {
        'Chromosome': [],
        'Start': [],
        'End': [],
        'GeneName': [],
        'CytogeneticLocations': []
    }

    for key, value in region_cyto_gene_locations.items():
        result_data['Chromosome'].append(key[0])
        result_data['Start'].append(key[1])
        result_data['End'].append(key[2])
        result_data['GeneName'].append(key[3])
        result_data['CytogeneticLocations'].append(','.join(value['CytogeneticLocations']))

    result_df = pd.DataFrame(result_data)

    # Save the updated DataFrame to the specified output file path
    result_df.to_csv(output_file_path, sep='\t', header=False, index=False)
                    
# Specify the output file path where you want to save the result
output_file_path = 'cyto_loc_gene_annotated_interval_list.csv'

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <interval_list_path> <cyto_loc_file_path> <output_file_path>")
        sys.exit(1)

    # Get the file paths from command-line arguments
    interval_list_path = sys.argv[1]
    cyto_loc_list_path = sys.argv[2]
    output_file_path = sys.argv[3]

# Call the function with the specified file paths
annotate_interval_file_with_cytolocation(interval_list_path, cyto_loc_list_path, output_file_path)

