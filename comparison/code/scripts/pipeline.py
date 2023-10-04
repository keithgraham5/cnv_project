import extraction
import manipulation
import plotting

# Run the data extraction process
filtered_parsed_data = extraction.extract_data()


# manipulation.manipulate_data()
normalised_lengths, transformed_scaled_data, = manipulation.manipulate_data(filtered_parsed_data)
print(normalised_lengths)
print(transformed_scaled_data)


# Run the plotting process
graph = plotting.build_and_plot_graph(normalised_lengths, transformed_scaled_data)