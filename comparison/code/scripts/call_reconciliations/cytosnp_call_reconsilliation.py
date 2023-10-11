import pandas as pd

cytosnp_data = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/cytosnp/data/processed_data/output_probe_data.csv'

# Define the normalize_call function
def normalize_call(row):
    if row['TYPE'] == 'NO CHANGE':
        return 'Normal'
    elif row['TYPE'] == 'LOSE':
        return 'Lose'
    elif row['TYPE'] == 'GAIN':
        return 'Gain'
    else:
        return 'Not Normalized'

def extract_data_from_cytosnp_source(cytosnp_data):
    # Read the data into a pandas DataFrame
    df = pd.read_csv(cytosnp_data)
    
    # Create a new column 'Call Normalization' and apply the normalize_call function to each row
    df['Call Normalization'] = df.apply(normalize_call, axis=1)
    
    return df

df = extract_data_from_cytosnp_source(cytosnp_data)
print(df.iloc[0])

# Return all unique values from the 'Call Normalization' column
unique_values = df['Call Normalization'].unique()

# Print the unique values
print(unique_values)