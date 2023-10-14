import pandas as pd

# Specify the file path
file_path = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/cytosnp/data/processed_data/output_probe_data.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path, delimiter=',', header=0)

# Convert the 'GeneName' column to string type
df['GeneName'] = df['GeneName'].astype(str)

# Split values in the 'GeneName' column by the '_' character and take the first part
df['New Column'] = df['GeneName'].str.split('_').str[0]

# Count the occurrences of "UNKNOWN" in the 'New Column'
unknown_count = (df['New Column'] == 'UNKNOWN').sum()

print("Number of 'UNKNOWN' occurrences in the 'New Column: {}".format(unknown_count))

# Assuming df is your DataFrame
# To list the unique values in the 'New Column
unique_values = df['New Column'].unique()

# To count the number of unique values
unique_count = len(unique_values)

# Print the results using .format()
print("Unique values in the 'New Column:")
print(unique_values)
print("Number of unique values in the 'New Column: {}".format(unique_count))
value_counts = df['New Column'].value_counts()
# Sort the counts in descending order (highest to lowest)
sorted_counts = value_counts.sort_values(ascending=False)
print(sorted_counts)
