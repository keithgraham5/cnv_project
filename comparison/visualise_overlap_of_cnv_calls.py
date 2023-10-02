# import matplotlib.pyplot as plt
# import mplcursors  # Import mplcursors
# from decimal import Decimal

# # Create a figure and axis
# fig, ax = plt.subplots()

# # Define chromosome lengths (you can customize this based on your data)
# chromosome_lengths = {
#     "chr1": (1, 249250621),
#     "chr2": (1, 243199373),
#     "chr3": (1, 198022430),
#     "chr4": (1, 191154276),
#     "chr5": (1, 180915260),
#     "chr6": (1, 171115067),
#     "chr7": (1, 159138663),
#     "chr8": (1, 146364022),
#     "chr9": (1, 141213431),
#     "chr10": (1, 135534747),
#     "chr11": (1, 135006516),
#     "chr12": (1, 133851895),
#     "chr13": (1, 115169878),
#     "chr14": (1, 107349540),
#     "chr15": (1, 102531392),
#     "chr16": (1, 90354753),
#     "chr17": (1, 81195210),
#     "chr18": (1, 78077248),
#     "chr19": (1, 59128983),
#     "chr20": (1, 63025520),
#     "chr21": (1, 48129895),
#     "chr22": (1, 51304566),
#     "chrX": (1, 155270560),
#     "chrY": (1, 59373566),
# }



# # Sample data for different datasets
# data_sources = {
# "call_data" : {
#     "chr1": (200000, 149000000, -0.2),
#     # Add data for other chromosomes if needed
# },

# "cnvkit_data" : {
#     "chr1": (1, 249250621, 0.1),
#     # "chr2": (1, 143199373, 0.3),
#     # Add data for other chromosomes if needed
# },

# "cnvrobot_data" : {
#     # "chr1": (1, 249250621, 0.05),
#     "chr1": (1, 24900000, 0.1),
#     # "chr2": (1, 143199373, 0.3),
#     # "chr3": (1, 198022430, 0.3),
#     # "chrX": (1,75270560, 0.1),
#     # "chrY": (1, 19373566, 0.12)
#     # Add data for other chromosomes if needed
# }
# }

import matplotlib.pyplot as plt
import mplcursors  # Import mplcursors
from decimal import Decimal
import matplotlib.cm as cm  # Import the color map module

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

# Sample data for different datasets
data_sources = [
    (
        "call_data",
        [
            ("chr1", (200000, 149000000, -0.2)),
            # Add data for other chromosomes if needed
        ],
    ),
    (
        "cnvkit_data",
        [
            ("chr1", (1, 249250621, 0.1)),
            ("chr2", (1, 143199373, 0.3))
            # Add data for other chromosomes if needed
        ],
    ),
    (
        "cnvrobot_data",
        [
            # ("chr1", (1, 249250621, 0.05)),
            # ("chr1", (1, 249250621, 0.1)),
            ("chr2", (1, 143199373, 0.2)),
            # ("chr3", (1, 198022430, 0.3)),
            ("chrX", (1, 75270560, 0.1)),
            ("chrY", (1, 19373566, 0.12))
            # Add data for other chromosomes if needed
        ],
    ),
]

# Define a mapping for 'X' and 'Y'
chromosome_mapping = {
    "chrX": "23",
    "chrY": "24",
}


class ChromosomeLengthNormaliser:
    def __init__(self, chromosome_lengths):
        """
        Initialize a ChromosomeLengthNormaliser object.

        Args:
            chromosome_lengths (dict): A dictionary containing chromosome lengths.
        """
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

        # Loop through each chromosome and its corresponding start and end positions
        for i, (chromosome, (start, end)) in enumerate(
            self.chromosome_lengths.items(), start=1
        ):

            # Calculate the length of the chromosome
            chromosome_length = end - start

            # Calculate the scaling factor for this chromosome (1 divided by chromosome length)
            scaling_factor = Decimal(1) / Decimal(chromosome_length)

            # Calculate the scaled start position based on the current index 'i'
            scaled_start = Decimal(i)

            # Calculate the scaled end position based on the scaling factor
            scaled_end = scaled_start + Decimal(chromosome_length) * scaling_factor

            # Store the normalized chromosome lengths in a dictionary
            self.normalised_chromosome_lengths[chromosome] = (
                scaled_start,
                scaled_end,
            )

            # Store the scaling factors for later reference
            self.scaling_factors[chromosome] = scaling_factor


class DataScaler:
    """
    A class for scaling data using provided scaling factors.
    """

    def __init__(self, data, scaling_factors):
        """
        Initialise a DataScaler object.

        Args:
            data (list): A list of tuples containing data to be scaled.
            scaling_factors (dict): A dictionary containing scaling factors for each chromosome.
        """
        self.data = data
        self.scaling_factors = scaling_factors
        self.scaled_data = []

    def scale_data(self):
        """
        Scale the data using provided scaling factors.

        This method scales the start and end positions of data for each chromosome
        based on the corresponding scaling factor and stores the scaled data.

        Returns:
            None
        """
        for source_name, source_data in self.data:
            scaled_source_data = []  # Create a list for storing scaled data
            for chromosome, (start, end, value) in source_data:
                # Get scaling factor for this chromosome from provided dictionary
                scaling_factor = self.scaling_factors[chromosome]

                # Scale the start and end positions using the scaling factor
                scaled_start = Decimal(start) * scaling_factor
                scaled_end = Decimal(end) * scaling_factor

                # Append the scaled data to the list
                scaled_source_data.append((chromosome, (scaled_start, scaled_end, value)))

            # Append the scaled source data to the list of scaled data
            self.scaled_data.append((source_name, scaled_source_data))


class DataTransformer:
    """
    A class for transforming and storing scaled data using chromosome mapping.
    """

    def __init__(self, scaled_data, chromosome_mapping):
        """
        Initialize a DataTransformer object.

        Args:
            scaled_data (list): A list of tuples containing the scaled data.
            chromosome_mapping (dict): A dictionary mapping chromosome names to their transformed values.
        """
        self.scaled_data = scaled_data
        self.chromosome_mapping = chromosome_mapping
        self.transformed_scaled_data = []

    def transform_and_store_data(self):
        """
        Transform and store the scaled sample data.

        This method takes the scaled data and applies a transformation based on the provided
        chromosome mapping. It then stores the transformed data.

        Returns:
            list: A list containing tuples of transformed and stored data.
        """
        for source_name, source_data in self.scaled_data:
            transformed_source_data = []  # Create a list for storing transformed data
            for chromosome, (start, end, call) in source_data:
                # Calculate transformed start and end positions based on chromosome mapping
                transformed_start = Decimal(start) + Decimal(
                    self.chromosome_mapping.get(chromosome, chromosome[3:])
                )
                transformed_end = Decimal(end) + Decimal(
                    self.chromosome_mapping.get(chromosome, chromosome[3:])
                )

                # Append the transformed data to the list
                transformed_source_data.append(
                    (chromosome, (transformed_start, transformed_end, call))
                )

            # Append the transformed source data to the list of transformed data
            self.transformed_scaled_data.append((source_name, transformed_source_data))


def set_x_axis_ticks_labels_vertical_lines(ax, normalised_chromosome_lengths):
    """
    Set the tick positions, labels, and vertical lines on the x-axis of a given 
    x axis.

    Args:
        ax (matplotlib.axes._axes.Axes): The Matplotlib axis on which to set the
        ticks and labels. normalised_chromosome_lengths (dict): A dictionary 
        containing chromosome lengths and their corresponding scaled positions.
    """
    # Extract the transformed start values as tick positions
    tick_positions = [float(start) for start, _ in normalised_chromosome_lengths.values()]

    # Set the tick positions, labels, and vertical lines on the x-axis
    ax.set_xticks(tick_positions)
    ax.set_xticklabels(normalised_chromosome_lengths.keys())
    for position in tick_positions:
        ax.axvline(x=position, color="gray", linestyle="--", linewidth=0.5)
    # Set the x-axis limits with an extension to include the Y chromosome
    ax.set_xlim(tick_positions[0], tick_positions[-1] + 1)


def set_y_axis_ticks_labels_lines(ax):
    """
    Set the Y-ticks, labels, limits, and add a horizontal line at the center of the Y-axis.

    Args:
        ax (matplotlib.axes._axes.Axes): The Matplotlib axis on which to set Y-axis properties.
    """
    # Set Y-ticks, labels
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels(["CNV losses", "0", "CNV gains"])
    # Set Y-axis limits to ensure a constant distance from -1, 0, and 1
    ax.set_ylim(-1.0, 1.0)
    # Add a horizontal line at the center of the Y-axis (where '0' is)
    ax.axhline(y=0, color="gray", linestyle="--", linewidth=0.5)


def plot_call_data(ax, transformed_scaled_data, color_map):
    """
    Plot call data on the given Matplotlib axis with different colors for each data set.

    Args:
        ax (matplotlib.axes._axes.Axes): The Matplotlib axis on which to plot 
        the data.
        transformed_scaled_data (list): A list of tuples containing 
        transformed and scaled call data for different data sets.
        color_map: The color map to use for generating distinct colors.

    Returns:
        None
    """
    for i, (source_name, source_data) in enumerate(transformed_scaled_data):
        color = color_map(i)  # Get a distinct color from the color map
        for chromosome, (start, end, call) in source_data:
            x_start = float(start)
            x_end = float(end)
            y_value = float(call)

            # Plot a line segment on the x-axis with the assigned color
            ax.plot([x_start, x_end], [y_value, y_value], marker='o', markersize=1, color=color)


# Define a color map to generate a sequence of distinct colors for your data sets:
color_map = plt.colormaps['tab10']  # You can choose a different color map if you prefer

# Create instances of the classes
normaliser = ChromosomeLengthNormaliser(chromosome_lengths)
scaler = DataScaler(data_sources, normaliser.scaling_factors)
transformer = DataTransformer(scaler.scaled_data, chromosome_mapping)

# Normalize chromosome lengths
normaliser.normalise_chromosome_lengths()
# Scale the call data
scaler.scale_data()
# Transform and store the scaled data
transformer.transform_and_store_data()

# Set X-axis ticks, labels, and vertical lines
set_x_axis_ticks_labels_vertical_lines(ax, normaliser.normalised_chromosome_lengths)
# Set Y-axis ticks, labels, limits, and horizontal line
set_y_axis_ticks_labels_lines(ax)
# Plot the call data with distinct colors
plot_call_data(ax, transformer.transformed_scaled_data, color_map)

# Display the plot
plt.show()








