import matplotlib.pyplot as plt

# Data
models = ['Random',  '2D CNN + LSTM', 'ResNet18 + LSTM', '3D CNN', '3D CNN + LSTM', 'ResNet + TCN', 'VGG16 + LSTM']
accuracies = [0.04, 0.138, 0.602, 0.676, 0.695, 0.778, 0.781]

# Create the bar graph
plt.figure(figsize=(10, 6))
plt.bar(models, accuracies, color='skyblue')

# Adding labels and title
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Accuracy of Different Models')



# Adding data labels on top of the bars
for i, v in enumerate(accuracies):
    plt.text(i, v + 0.01, str(v), ha='center', va='bottom')

# Setting y-axis limit to [0, 1]
plt.ylim(0, 1)

# Show the plot
plt.show()
