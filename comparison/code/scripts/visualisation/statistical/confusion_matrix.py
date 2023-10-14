import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix

# Replace these with your actual predicted and true labels
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
y_pred = [1, 0, 1, 0, 1, 1, 0, 1, 1, 0]

# Calculate the confusion matrix
cm = confusion_matrix(y_true, y_pred)



# Create a heatmap of the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", linewidths=.5)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")

# Customize the axis labels based on your class names
class_names = ["Class 0", "Class 1"]
tick_marks = [0.5, 1.5]
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

plt.show()