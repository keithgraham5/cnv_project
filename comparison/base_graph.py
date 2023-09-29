import matplotlib.pyplot as plt
import numpy as np

# Create a list of CNV values
cnv_call_values = [-1.0, 0, 1]


# Create a list of chromosome positions
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



# Total lenght of all chromosomes 
# Set X-axis limits
ax.set_xlim(0, current_position)  # Set the X-axis limit to the total length of all chromosomes

# Create a scatter plot of the CNV values versus the chromosome positions
plt.scatter(chromosome_positions, cnv_values)

# Set the x-axis label
plt.xlabel("Chromosome Position")

# Set the y-axis label
plt.ylabel("CNV Value")

# Set the title of the plot
plt.title("CNV Data Scatter Plot")

# Display the plot
plt.show()