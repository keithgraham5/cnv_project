import extraction
import manipulation 
# import plotting

# Run the data manipluation process
data_sources = extraction.data_sources
print(data_sources)

# Run the manipulation process 
data_plots = manipulation(data_sources)

# # Run the plotting process
# plotting(normalised_chromosome_lengths, transfored_scaled_data)