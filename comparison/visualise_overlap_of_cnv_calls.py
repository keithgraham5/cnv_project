import matplotlib.pyplot as plt
import mplcursors  # Import mplcursors
from decimal import Decimal

# Create a figure and axis
fig, ax = plt.subplots()

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
# call_data = {
#     "chr1": (200000, 149000000, -0.2),
#     "chr2": (1, 143199373, 0.3),
#     "chr3": (1, 198022430, 0.3),
#     "chrX": (1,75270560, 0.1),
#     "chrY": (1, 19373566, 0.12)
#     # Add data for other chromosomes if needed
# }

# # Sample data for different datasets
# snp_data = {
#     "chr1": (200000, 149000000, -0.2),
#     "chr2": (1, 143199373, 0.3),
#     "chr3": (1, 198022430, 0.3),
#     "chrX": (1,75270560, 0.1),
#     "chrY": (1, 19373566, 0.12)
#     # Add data for other chromosomes if needed
# }

# cnvkit_data = {
#     "chr1": (1, 249250621, 0.1),
#     "chr2": (1, 143199373, 0.3),
#     "chr3": (1, 198022430, 0.3),
#     "chrX": (1,75270560, 0.1),
#     "chrY": (1, 19373566, 0.12)
#     # Add data for other chromosomes if needed
# }

# cnvrobot_data = {
#     "chr1": (1, 249250621, 0.05),
#     "chr1": (1, 249250621, 0.1),
#     "chr2": (1, 143199373, 0.3),
#     "chr3": (1, 198022430, 0.3),
#     "chrX": (1,75270560, 0.1),
#     "chrY": (1, 19373566, 0.12)
#     # Add data for other chromosomes if needed
# }

# # Define a mapping for 'X' and 'Y'
# chromosome_mapping = {
#     "chrX": "23",
#     "chrY": "24",
# }




class ChromosomeLengthNormaliser:
    def __init__(self, chromosome_lengths):
        self.chromosome_lengths = chromosome_lengths
        self.normalised_chromosome_lengths = {}
        self.scaling_factors = {}
    
    def normalise_chromosome_lengths(self):
        """
        Normalize each chromosome's length to a whole number.
        
        Args:
            chromosome_lengths (dict): A dictionary containing chromosome lengths.

        Returns:
            tuple: A tuple containing two dictionaries: normalised_chromosome_lengths
            and scaling_factors.
        """
        # normalised_chromosome_lengths = {}
        # scaling_factors = {}

        for i, (chromosome, (start, end)) in enumerate(self.chromosome_lengths.items(), start=1):
            chromosome_length = end - start
            scaling_factor = Decimal(1) / Decimal(chromosome_length)
            scaled_start = Decimal(i)
            scaled_end = scaled_start + Decimal(chromosome_length) * scaling_factor
            self.normalised_chromosome_lengths[chromosome] = (scaled_start, scaled_end)
            self.scaling_factors[chromosome] = scaling_factor  # Update the global scaling_factors
            print(f"Chromosome: {chromosome}")
            print(f"Original Length: {chromosome_length}")
            print(f"Scaling Factor: {scaling_factor}")
            print(f"Scaled Start: {scaled_start}")
            print(f"Scaled End: {scaled_end}")

            
# Create instances of the classes 
normaliser = ChromosomeLengthNormaliser(chromosome_lengths)

# Call the normlaised_chromosome_lengths method 
normaliser.normalise_chromosome_lengths()



# def scale_call_data(call_data, scaling_factors):
#     """
#     Scale call data based on provided scaling factors.

#     This function takes a dictionary of SNP data and a dictionary of scaling factors
#     for each chromosome. It scales the start and end positions of each SNP data point
#     using the corresponding scaling factor and returns a dictionary containing the scaled data.

#     Parameters:
#     - snp_data (dict): A dictionary where keys are chromosome names and values are tuples
#       containing (start, end, value) for each SNP data point.
#     - scaling_factors (dict): A dictionary where keys are chromosome names and values are
#       scaling factors used for each chromosome.

#     Returns:
#     - dict: A dictionary containing the scaled SNP data with the same structure as snp_data.
#     """
#     # Create an empty dictionary to store the scaled data
#     scaled_data = {}
    
#     # Loop through each chromosome and its corresponding data
#     for chromosome, (start, end, value) in call_data.items():
#         # Get the scaling factor for this chromosome from the provided dictionary
#         scaling_factor = scaling_factors[chromosome]
        
#         # Scale the start and end positions using the scaling factor
#         scaled_start = Decimal(start) * scaling_factor
#         scaled_end = Decimal(end) * scaling_factor
        
#         # Store the scaled data in the dictionary
#         scaled_data[chromosome] = (scaled_start, scaled_end, value)
    
#     # Return the dictionary containing the scaled data
#     return scaled_data


# def transform_and_store_data(scaled_data, chromosome_mapping):
#     """
#     Transform and store the scaled sample data.

#     Args:
#         scaled_data (dict): A dictionary containing the scaled data.
#         chromosome_mapping (dict): A dictionary mapping chromosome names to their transformed values.

#     Returns:
#         dict: A dictionary containing the transformed and stored data.
#     """
#     transformed_scaled_data = {}

#     for chromosome, (start, end, call) in scaled_data.items():
#         transformed_start = Decimal(start) + Decimal(chromosome_mapping.get(chromosome, chromosome[3:]))
#         transformed_end = Decimal(end) + Decimal(chromosome_mapping.get(chromosome, chromosome[3:]))
#         transformed_scaled_data[chromosome] = (transformed_start, transformed_end, call)

#     return transformed_scaled_data


# def set_x_axis_ticks_labels_vertical_lines(ax, normalised_chromosome_lengths):
#     """
#     Set the tick positions, labels and vertical lines on the x-axis of a given 
#     x axis.

#     Args:
#         ax (matplotlib.axes._axes.Axes): The Matplotlib axis on which to set the
#         ticks and labels. normalised_chromosome_lengths (dict): A dictionary 
#         containing chromosome lengths and their corresponding scaled positions.
#     """
#     # Extract the transformed start values as tick positions
#     tick_positions = [float(start) for start, _ in normalised_chromosome_lengths.values()]

#     # Set the tick positions, labels and vertical lines on the x-axis
#     ax.set_xticks(tick_positions)
#     ax.set_xticklabels(normalised_chromosome_lengths.keys())
#     for position in tick_positions:
#         ax.axvline(x=position, color='gray', linestyle='--', linewidth=0.5)
#     # Set the x axis limits with extension to include the Y chromosome 
#     ax.set_xlim(tick_positions[0], tick_positions[-1]+1)
    
# def set_y_axis_ticks_labels_lines(ax):
#     """
#     Set the Y-ticks, labels, limits, and add a horizontal line at the center of the Y-axis.

#     Args:
#         ax (matplotlib.axes._axes.Axes): The Matplotlib axis on which to set Y-axis properties.
#     """
#     # Set Y-ticks, lables
#     ax.set_yticks([-1, 0, 1])
#     ax.set_yticklabels(['CNV losses', '0', 'CNV gains'])
#     # Set Y-axis limtes to ensure a constant distance from -1, 0, and 1
#     ax.set_ylim(-1.0, 1.0)
#     # Add a horizontal line at the center of the Y-axis (where '0' is
#     ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
    
# def plot_call_data(ax, transformed_scaled_data):
#     """
#     Plot call data on the given Matplotlib axis.

#     Args:
#         ax (matplotlib.axes._axes.Axes): The Matplotlib axis on which to plot 
#         the data. transformed_scaled_data (dict): A dictionary containing 
#         transformed and scaled call data.

#     Returns:
#         None
#     """
#     for chromosome, (start, end, call) in transformed_scaled_data.items():
#         x_start = float(start)
#         x_end = float(end)
#         y_value = float(call)
        
#         # Plot a line segment on the x-axis
#         ax.plot([x_start, x_end], [y_value, y_value], marker='o', markersize=1)



# # Noralise chromosome lengths and calculate scaling factors 
# normalised_chromosome_lengths, scaling_factors = normalise_chromosome_lengths(chromosome_lengths)
# # Scale the call data using scaling factors derived from normlaisation of chromosome lengths
# scaled_data =  scale_call_data(call_data, scaling_factors)
# # Transform and store the scaled data
# transformed_scaled_data = transform_and_store_data(scaled_data, chromosome_mapping)
# # Set X-axis ticks, labels, and vertical lines
# x_tick_and_labels = set_x_axis_ticks_labels_vertical_lines(ax, normalised_chromosome_lengths)
# # Set Y-axis ticks, labels, limits, and horizontal line
# y_tick_and_lables = set_y_axis_ticks_labels_lines(ax)
# # Plot the call data
# plots = plot_call_data(ax, transformed_scaled_data)
# 
# Display the plot
# plt.show()










