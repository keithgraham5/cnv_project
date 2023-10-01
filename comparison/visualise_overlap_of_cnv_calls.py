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

def normalise_chromosome_lengths(chromosome_lengths):
    """
    Normalize each chromosome's length to a whole number.
    
    Args:
        chromosome_lengths (dict): A dictionary containing chromosome lengths.

    Returns:
        tuple: A tuple containing two dictionaries: normalised_chromosome_lengths
        and scaling_factors.
    """
    normalised_chromosome_lengths = {}
    scaling_factors = {}

    for i, (chromosome, (start, end)) in enumerate(chromosome_lengths.items(), start=1):
        chromosome_length = end - start
        scaling_factor = Decimal(1) / Decimal(chromosome_length)
        scaled_start = Decimal(i)
        scaled_end = scaled_start + Decimal(chromosome_length) * scaling_factor
        normalised_chromosome_lengths[chromosome] = (scaled_start, scaled_end)
        scaling_factors[chromosome] = scaling_factor

    return normalised_chromosome_lengths, scaling_factors

# Example usage:
chromosome_lengths = {
    "chr1": (1, 249250621),
    # Add data for other chromosomes if needed
}

normalized_lengths, factors = normalize_chromosome_lengths(chromosome_lengths)
print(normalized_lengths)
print(factors)







# Sample data for different datasets
snp_data = {
    "chr1": (200000, 149000000, -0.2),
    "chr2": (1, 143199373, 0.3),
    "chr3": (1, 198022430, 0.3),
    "chrX": (1,75270560, 0.1),
    "chrY": (1, 19373566, 0.12)
    # Add data for other chromosomes if needed
}

cnvkit_data = {
    "chr1": (1, 249250621, 0.1),
    "chr2": (1, 143199373, 0.3),
    "chr3": (1, 198022430, 0.3),
    "chrX": (1,75270560, 0.1),
    "chrY": (1, 19373566, 0.12)
    # Add data for other chromosomes if needed
}

cnvrobot_data = {
    "chr1": (1, 249250621, 0.05),
    "chr1": (1, 249250621, 0.1),
    "chr2": (1, 143199373, 0.3),
    "chr3": (1, 198022430, 0.3),
    "chrX": (1,75270560, 0.1),
    "chrY": (1, 19373566, 0.12)
    # Add data for other chromosomes if needed
}

# Scale start and end positions of SNP data based on the scaling factors
scaled_data = {}
for chromosome, (start, end, value) in snp_data.items():
    scaling_factor = scaling_factors[chromosome]  # Get the scaling factor for this chromosome
    scaled_start = Decimal(start) * scaling_factor
    scaled_end = Decimal(end) * scaling_factor
    scaled_data[chromosome] = (scaled_start, scaled_end, value)
    print(f"scaled_data = {scaled_data}")

# Define a mapping for 'X' and 'Y'
chromosome_mapping = {
    "chrX": "23",
    "chrY": "24",
}

# Convert and store the transformed sample data
transformed_scaled_data = {}
for chromosome, (start, end, call) in scaled_data.items():
    transformed_start = Decimal((start)) + Decimal(chromosome_mapping.get(chromosome, chromosome[3:]))
    transformed_end = Decimal((end)) + Decimal(chromosome_mapping.get(chromosome, chromosome[3:]))
    transformed_scaled_data[chromosome] = (transformed_start, transformed_end, call)
    print(transformed_scaled_data)
# Sanity check 
# print(transformed_scaled_data)


# Extract the tranformed start values as tick positions 
tick_positions = [float(start) for start, _ in 
                  normalised_chromosome_lengths.values()]


# Set tjhe tick positions and labels on the x-axis
ax.set_xticks(tick_positions)
ax.set_xticklabels(normalised_chromosome_lengths.keys())


# Create vertical lines at tick positions
for position in tick_positions:
    # Sanity check
    # print(f"tick positions = {position}")
    ax.axvline(x=position, color='gray', linestyle='--', linewidth=0.5)
    
    

# # # Add vertical lines at the end postions of chromosomes


# Set the x axis limits with extension to include the Y chromosome 
ax.set_xlim(tick_positions[0], tick_positions[-1]+1)
print(tick_positions)


# Set Y-ticks, lables
ax.set_yticks([-1, 0, 1])
ax.set_yticklabels(['CNV losses', '0', 'CNV gains'])

# Set Y-axis limtes to ensure a constant distance from -1, 0, and 1
ax.set_ylim(-1.0, 1.0)

# Add a horizontal line at the center of the Y-axis (where '0' is)
ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)


# # Plot SNP data start, end on X-axis call on the Y axis  
for chromosome, (start, end, call) in transformed_scaled_data.items():
    x_start = float(start)
    print(x_start)
    x_end =float(end)
    y_value = float(call)
    
    # Plot a line segment on the x-axis 
    ax.plot([x_start, x_end], [y_value, y_value], marker='o', markersize=1)



# Display the plot
plt.show()

# # Add a horizontal line at the center of the Y-axis (where '0' is)
# ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)

# # Set Y-axis limits to ensure a constant distance from -1, 0, and 1
# ax.set_ylim(-1.0, 1.0)

# # Set chromosome labels and limits on the X-axis
# chromosome_ticks = []
# chromosome_labels = []
# chromosome_end_lines = []
# chromosome_start_lines = []

# current_position = 0

# for chromosome, (start, end) in chromosome_lengths.items():
#     chromosome_length = end - start
#     chromosome_ticks.append(current_position + (chromosome_length / 2))  # Place the label in the middle of each chromosome
#     chromosome_labels.append(chromosome)
#     chromosome_start_lines.append(current_position)
#     chromosome_end_lines.append(current_position + chromosome_length)
#     current_position += chromosome_length
# print(f"chr_start_lines are {chromosome_start_lines}")
# print(f"chr_end_lines are {chromosome_end_lines}")
# ax.set_xticks(chromosome_ticks)
# ax.set_xticklabels(chromosome_labels, rotation=0, ha='center')

# # Set X-axis limits
# ax.set_xlim(0, current_position)

# # Draw vertical lines at chromosome ends
# for x_pos in chromosome_end_lines:
#     ax.axvline(x_pos, color='gray', linestyle='--', linewidth=0.5)

# # Plot SNP data with tooltips
# for chromosome, data_points in snp_data.items():
#     for start, end, value in data_points:
#         chromosome_length = chromosome_lengths[chromosome][1] - chromosome_lengths[chromosome][0]
#         x_position = current_position * ((start - chromosome_lengths[chromosome][0]) / chromosome_length) + chromosome_start_lines[chromosome_labels.index(chromosome)]
#         scatter = ax.scatter(x_position, value, marker='o', color='blue', alpha=0.5, label='SNP Data')
#         mplcursors.cursor(scatter).connect(
#             "add", lambda sel, chromosome=chromosome, start=start, end=end, value=value: sel.annotation.set_text(f"Chromosome: {chromosome}\nStart: {start}\nEnd: {end}\nValue: {value}"))

# # Set labels and title
# ax.set_xlabel("Chromosomes")
# ax.set_title("CNV Calls on Chromosomes")

# # Move the legend inside the graph to the upper right corner
# ax.legend(loc='upper right')









