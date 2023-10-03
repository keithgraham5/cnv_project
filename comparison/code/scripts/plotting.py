
import matplotlib.pyplot as plt
import mplcursors  # Import mplcursors
from decimal import Decimal
import matplotlib.cm as cm  # Import the color map module

import manipulation

# Set X-axis ticks, labels, and vertical lines
set_x_axis_ticks_labels_vertical_lines(ax, normaliser.normalised_chromosome_lengths)
# Set Y-axis ticks, labels, limits, and horizontal line
set_y_axis_ticks_labels_lines(ax)
# Plot the call data with distinct colors
plot_call_data(ax, transformer.transformed_scaled_data)




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


def plot_call_data(ax, transformed_scaled_data):
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
    primary_colours = ['red', 'blue', 'green']
    
    for i, (source_name, source_data) in enumerate(transformed_scaled_data):
        color = primary_colours[i % len(primary_colours)]  # Get a distinct color from the color map
        for chromosome, (start, end, call) in source_data:
            x_start = float(start)
            x_end = float(end)
            y_value = float(call)

            # Plot a line segment on the x-axis with the assigned color
            ax.plot([x_start, x_end], [y_value, y_value], marker='o', markersize=1, color=color)
            
# # Set X-axis ticks, labels, and vertical lines
# set_x_axis_ticks_labels_vertical_lines(ax, normaliser.normalised_chromosome_lengths)
# # Set Y-axis ticks, labels, limits, and horizontal line
# set_y_axis_ticks_labels_lines(ax)
# # Plot the call data with distinct colors
# plot_call_data(ax, transformer.transformed_scaled_data)

# # Display the plot
# plt.show()