


import pandas as pd
import io
import sys

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



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_file_path>")
        sys.exit(1)

    snp_csv_file_path = sys.argv[1]
    df_snp_1 = read_csv_from_probe_id(snp_csv_file_path)
    
    if df_snp_1 is not None:
        # Process the DataFrame as needed
        print(df_snp_1.head())  # For example, print the first few rows