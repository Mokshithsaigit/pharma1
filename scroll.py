import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a pandas dataframe
df = pd.read_csv('quantity.csv')

# Extract the medicine names and corresponding quantities
medicine_names = df['medicine_name'].tolist()
quantities = df['quantity'].tolist()

# Calculate the total quantity
total_quantity = sum(quantities)

# Calculate the percentage of each medicine in the inventory
percentages = [q/total_quantity * 100 for q in quantities]

# Create the pie chart
plt.pie(percentages, labels=medicine_names, autopct='%1.1f%%')
plt.title('Medicine Inventory')
plt.axis('equal')

# Show the plot
plt.show()
