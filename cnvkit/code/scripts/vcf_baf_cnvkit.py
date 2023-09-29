import argparse
import vcf

# def convert_vcf_to_baf(input_vcf_path, output_baf_path):
#     try:
#         # Open the VCF file
#         vcf_file = vcf.Reader(filename=input_vcf_path)
#
#         # Create a BAF file
#         with open(output_baf_path, 'w') as baf_file:
#             # Write a header to the BAF file (customize as needed)
#             baf_file.write("#CHROM\tPOS\tSAMPLE\tBAF\n")
#
#             # Iterate through variants in the VCF
#             for record in vcf_file:
#                 for sample in record.samples:
#                     # Calculate BAF
#                     total_reads = sample['AD'][0] + sample['AD'][1]  # Total reads at variant position
#                     if total_reads > 0:
#                         baf = sample['AD'][1] / total_reads  # BAF calculation
#                     else:
#                         baf = None  # Handle cases with no reads
#
#                     # Write BAF information to the BAF file
#                     baf_file.write(f"{record.CHROM}\t{record.POS}\t{sample.sample}\t{baf}\n")
#
#         print(f"Conversion completed. BAF file saved to {output_baf_path}")
#
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#
# if __name__ == "__main__":
#     # Create argument parser
#     parser = argparse.ArgumentParser(description="Convert VCF to BAF")
#
#     # Add arguments for input VCF and output BAF file paths
#     parser.add_argument("input_vcf", help="Path to the input VCF file")
#     parser.add_argument("output_baf", help="Path to the output BAF file")
#
#     # Parse command-line arguments
#     args = parser.parse_args()
#
#     # Call the function to convert VCF to BAF
#     convert_vcf_to_baf(args.input_vcf, args.output_baf)

import argparse
import vcf

def extract_baf_from_vcf(input_vcf_path, output_baf_path):
    try:
        # Open the VCF file
        vcf_file = vcf.Reader(filename=input_vcf_path)

        # Create a BAF file
        with open(output_baf_path, 'w') as baf_file:
            # Write the header to the BAF file
            baf_file.write("chromosome\tstart\tend\tgene\tlog2\tSAMPLE\tBAF\n")

            # Iterate through variants in the VCF
            for record in vcf_file:
                for sample in record.samples:
                    # Calculate BAF
                    total_reads = sum(sample['AD'])  # Total reads at variant position
                    if total_reads > 0:
                        baf = sample['AD'][1] / total_reads  # BAF calculation
                    else:
                        baf = None  # Handle cases with no reads

                    # Write BAF information to the BAF file
                    baf_file.write(f"{record.CHROM}\t{record.POS}\t{record.POS}\t.\t.\t{sample.sample}\t{baf}\n")

        print(f"Conversion completed. BAF file saved to {output_baf_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Extract BAF from VCF")

    # Add arguments for input VCF and output BAF file paths
    parser.add_argument("input_vcf", help="Path to the input VCF file")
    parser.add_argument("output_baf", help="Path to the output BAF file")

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the function to extract BAF from VCF
    extract_baf_from_vcf(args.input_vcf, args.output_baf)