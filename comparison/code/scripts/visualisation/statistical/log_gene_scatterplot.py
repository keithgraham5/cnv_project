import numpy as np
import matplotlib.pyplot as plt

# Sample data for multiple genes
genes = ["Gene1", "Gene2", "Gene3", "Gene4", "Gene5"]
caller1_scores = [2.3, 3.1, 1.9, 4.0, 2.7]
caller2_scores = [2.8, 2.9, 3.2, 2.1, 2.5]
caller3_scores = [3.1, 3.4, 3.0, 2.8, 2.6]

# Calculate log2 scores for each caller
log2_caller1 = [np.log2(score) for score in caller1_scores]
log2_caller2 = [np.log2(score) for score in caller2_scores]
log2_caller3 = [np.log2(score) for score in caller3_scores]
plt.figure(figsize=(10, 6))

# Create scatter plots for each caller
plt.scatter(genes, log2_caller1, label='Caller 1', color='blue', marker='o')
plt.scatter(genes, log2_caller2, label='Caller 2', color='green', marker='s')
plt.scatter(genes, log2_caller3, label='Caller 3', color='red', marker='^')

plt.xlabel('Genes')
plt.ylabel('Log2 Scores')
plt.title('Comparison of Log2 Scores from Three Callers')
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.tight_layout()  # Ensure all elements fit within the plot area

plt.show()