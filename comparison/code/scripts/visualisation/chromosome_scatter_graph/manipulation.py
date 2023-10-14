import matplotlib.pyplot as plt
import mplcursors  # Import mplcursors
from decimal import Decimal
import matplotlib.cm as cm  # Import the color map module



# Define chromosome lengths (you can customize this based on your data)
chromosome_lengths = {
    "chr1": (1, 249250621),
    "chr2": (1, 243199373),
    "chr3": (1, 198022430),
    "chr4": (1, 191154276),
    "chr5": (1, 180915260),
    "chr6": (1, 171115067),
    "chr7": (1, 159138663),
    "chr8": (1, 146364022),
    "chr9": (1, 141213431),
    "chr10": (1, 135534747),
    "chr11": (1, 135006516),
    "chr12": (1, 133851895),
    "chr13": (1, 115169878),
    "chr14": (1, 107349540),
    "chr15": (1, 102531392),
    "chr16": (1, 90354753),
    "chr17": (1, 81195210),
    "chr18": (1, 78077248),
    "chr19": (1, 59128983),
    "chr20": (1, 63025520),
    "chr21": (1, 48129895),
    "chr22": (1, 51304566),
    "chrX": (1, 155270560),
    "chrY": (1, 59373566),
}


# # Sample data for different datasets
# data_sources = [
#     (
#         "call_data",
#         [
#             ("chr1", (200000, 149000000, -0.2)),
#             # Add data for other chromosomes if needed
#         ],
#     ),
#     (
#         "cnvkit_data",
#         [
#             ("chr1", (1, 249250621, 0.1)),
#             # ("chr2", (1, 143199373, 0.3))
#             # Add data for other chromosomes if needed
#         ],
#     ),
#     (
#         "cnvrobot_data",
#         [
#             # ("chr1", (1, 249250621, 0.05)),
#             # ("chr1", (1, 249250621, 0.1)),
#             # ("chr2", (1, 143199373, 0.2)),
#             # ("chr3", (1, 198022430, 0.3)),
#             ("chrX", (1, 75270560, 0.1)),
#             ("chrY", (1, 19373566, 0.12))
#             # Add data for other chromosomes if needed
#         ],
#     ),
# ]

# Define a mapping for 'X' and 'Y'
chromosome_mapping = {
    "chrX": "23",
    "chrY": "24",
}


def normalise_chromosome_lengths(chromosome_lengths):
    """
    Normalize chromosome lengths to whole numbers.

    Args:
        chromosome_lengths (dict): A dictionary containing chromosome lengths.

    Returns:
        tuple: A tuple containing two dictionaries: normalised_chromosome_lengths
        and scaling_factors.
    """
    normalised_chromosome_lengths = {}
    scaling_factors = {}
    

    # Loop through each chromosome and its corresponding start and end positions
    for i, (chromosome, (start, end)) in enumerate(chromosome_lengths.items(), start=1):
        # Calculate the length of the chromosome
        chromosome_length = end - start

        # Calculate the scaling factor for this chromosome (1 divided by chromosome length)
        scaling_factor = Decimal(1) / Decimal(chromosome_length)

        # Calculate the scaled start position based on the current index 'i'
        scaled_start = Decimal(i)

        # Calculate the scaled end position based on the scaling factor
        scaled_end = scaled_start + Decimal(chromosome_length) * scaling_factor

        # Store the normalized chromosome lengths in a dictionary
        normalised_chromosome_lengths[chromosome] = (scaled_start, scaled_end)

        # Store the scaling factors for later reference
        scaling_factors[chromosome] = scaling_factor
        

    return normalised_chromosome_lengths, scaling_factors
    

def scale_data(data, scaling_factors):
    """
    Scale the data using provided scaling factors.

    Args:
        data (list): A list of tuples containing data to be scaled.
        scaling_factors (dict): A dictionary containing scaling factors for each chromosome.

    Returns:
        list: A list of scaled data.
    """
    scaled_data = []

    for source_name, source_data in data:
        scaled_source_data = []  # Create a list for storing scaled data
        for chromosome, (start, end, value) in source_data:
            # Get scaling factor for this chromosome from the provided dictionary
            scaling_factor = scaling_factors[chromosome]

            # Scale the start and end positions using the scaling factor
            scaled_start = Decimal(start) * scaling_factor
            scaled_end = Decimal(end) * scaling_factor

            # Append the scaled data to the list
            scaled_source_data.append((chromosome, (scaled_start, scaled_end, value)))

        # Append the scaled source data to the list of scaled data
        scaled_data.append((source_name, scaled_source_data))

    return scaled_data



def transform_and_store_data(scaled_data, chromosome_mapping):
    """
    Transform and store the scaled sample data.

    Args:
        scaled_data (list): A list of tuples containing the scaled data.
        chromosome_mapping (dict): A dictionary mapping chromosome names to their transformed values.

    Returns:
        list: A list containing tuples of transformed and stored data.
    """
    transformed_scaled_data = []

    for source_name, source_data in scaled_data:
        transformed_source_data = []  # Create a list for storing transformed data
        for chromosome, (start, end, call) in source_data:
            # Calculate transformed start and end positions based on chromosome mapping
            transformed_start = Decimal(start) + Decimal(
                chromosome_mapping.get(chromosome, chromosome[3:])
            )
            transformed_end = Decimal(end) + Decimal(
                chromosome_mapping.get(chromosome, chromosome[3:])
            )

            # Append the transformed data to the list
            transformed_source_data.append(
                (chromosome, (transformed_start, transformed_end, call))
            )

        # Append the transformed source data to the list of transformed data
        transformed_scaled_data.append((source_name, transformed_source_data))
    print(transformed_scaled_data)

    return transformed_scaled_data


def manipulate_data(filtered_parsed_data):
    normalised_lengths, scaling_factors = normalise_chromosome_lengths(chromosome_lengths)
    scaled_data = scale_data(filtered_parsed_data, scaling_factors)
    transformed_data = transform_and_store_data(scaled_data, chromosome_mapping)
    
    return normalised_lengths, transformed_data



