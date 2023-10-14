import pandas as pd

# Specify the file path
file_path = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/data/reference_data/20220207_PanHaemOnc.bed'

# Read the BED file into a Pandas DataFrame
df = pd.read_csv(file_path, delimiter='\t', header=None, names=['Column1', 'Column2', 'Column3', '4th Column', '...'])

# Split values in the 4th column by the '_' character and take the first part
df['New Column'] = df['4th Column'].str.split('_').str[0]

# Count the occurrences of "UNKNOWN" in the 'New Column'
unknown_count = (df['New Column'] == 'UNKNOWN').sum()

print("Number of 'UNKNOWN' occurrences in the 'New Column: {}".format(unknown_count))

# Assuming df is your DataFrame
# To list the unique values in the 4th column
unique_values = df['New Column'].unique()

# To count the number of unique values
unique_count = len(unique_values)

# Print the results using .format()
print("Unique values in the 4th column:")
print(unique_values)
print("Number of unique values in the 4th column: {}".format(unique_count))
value_counts = df['New Column'].value_counts()
# Sort the counts in descending order (highest to lowest)
sorted_counts = value_counts.sort_values(ascending=False)
print(sorted_counts)


# Get the top 20 unique values from the sorted counts
top_20_values = sorted_counts.head(30)

# Print the top 20 unique values
print("Top 20 unique values in the 'New Column':")
print(top_20_values)