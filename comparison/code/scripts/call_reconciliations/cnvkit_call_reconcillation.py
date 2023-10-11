import pandas as pd 

cnv_data = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/cnvkit/data/processed_data/intermediate/H28194-21.sorted.dedup.recalibrated.Tumor.call.cns'

def extract_data_from_cnvkit_source(cnvkit_data):
    # Read the data into a pandas DataFrame
    df = pd.read_csv(cnvkit_data, delimiter="\t")
    
    # Create a new column 'Call Normalization' and assign a default value to it (e.g., 'Not Normalized')
    df['Call Normalization'] = 'Not Normalized'
    
    # Function to add 'Normal,' 'Lose,' or 'Gain' based on 'cn' value
    def normalize_call(row):
        if row['cn'] == 2:
            return 'Normal'
        elif row['cn'] < 2:
            return 'Lose'
        else:
            return 'Gain'
    
    # Apply the function to each row and create the 'Call Normalisation' column
    df['Call Normalization'] = df.apply(normalize_call, axis=1)
    
    return df

df = extract_data_from_cnvkit_source(cnv_data)
