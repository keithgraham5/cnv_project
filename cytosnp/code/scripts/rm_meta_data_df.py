import pandas as pd
import io
import argparse
import os

# Define the input and output directories
INPUT_DIR = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/cytosnp/data/raw_data/'
OUTPUT_DIR = '/home/keith/BIOL61860_research_project_in_clinical_bioinformatics/cnv_project/cytosnp/data/processed_data/intermediate/'

def tidy_probe_list(input_file_name, output_file_name):
    input_data_path = os.path.join(INPUT_DIR, input_file_name)
    output_data_path = os.path.join(OUTPUT_DIR, output_file_name)

    column_headers = [
        'PROBE ID', 'AMPCH1', 'AMPCH2', 'PROCESSED LOG R RATIO',
        'B ALLELE FREQUENCY', 'LOG R PRODUCT', 'LOG R RATIO',
        'GENOTYPE', 'CHROMOSOME', 'POSITION', 'COPY #', 'TYPE',
        'CYTO LOCN', 'GC CONTENT'
    ]

    start_reading = False
    data_lines = []

    with open(input_data_path, 'r') as file:
        for line in file:
            if start_reading:
                data_lines.append(line.strip())
            elif 'PROBE ID' in line:
                start_reading = True

    if data_lines:
        data_str = '\n'.join(data_lines)
        df = pd.read_csv(io.StringIO(data_str), delimiter='\t', names=column_headers, header=None)
        
        # Save the DataFrame as a CSV file in the output directory
        df.to_csv(output_data_path, index=False)
        return df
    else:
        print("No 'PROBE ID' data found in the CSV file.")
        return None

def main():
    parser = argparse.ArgumentParser(description='Process a CSV file and extract data starting from "PROBE ID".')
    parser.add_argument('input_file_name', type=str, help='Input file name (located in the input directory).')
    parser.add_argument('output_file_name', type=str, help='Output file name (saved in the output directory).')

    args = parser.parse_args()
    input_file_name = args.input_file_name
    output_file_name = args.output_file_name

    df = tidy_probe_list(input_file_name, output_file_name)
    if df is not None:
        print("Data extracted successfully.")
        print(df)

if __name__ == '__main__':
    main()

