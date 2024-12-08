import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load the data set
data = pd.read_csv("D:/AI Mastery/data/benin-malanville.csv")


#Display basic info
print (data.info())
print (data.head())

"""# Generate summary statistics for numeric columns
summary_stats = data.describe()
print("Summary Statistics:\n\n", summary_stats)


# Select numeric columns only
numeric_data = data.select_dtypes(include=['number'])

# Calculate mean, median, and standard deviation for numeric columns
mean_values = numeric_data.mean()
median_values = numeric_data.median()
std_values = numeric_data.std()

print("Mean Values:\n", mean_values)
print("\nMedian Values:\n", median_values)
print("\nStandard Deviation Values:\n", std_values)
"""

"""# Check for missing values
missing_values = data.isnull().sum()
print("\nMissing Values:\n", missing_values)

# Check for negative values in GHI, DNI, and DHI
columns_to_check = ['GHI', 'DNI', 'DHI']
for column in columns_to_check:
    negative_values = data[data[column] < 0]
    print(f"\nNegative values in {column}:\n", negative_values)

# Visualize outliers using boxplots for GHI, DNI, and DHI

for column in ['ModA', 'ModB', 'WS', 'WSgust']:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=data[column])
    plt.title(f"Box Plot of {column}")
    plt.show()"""


# Convert 'Timestamp' to datetime format
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Set the Timestamp column as the index
data.set_index('Timestamp', inplace=True)

# Plot time series for GHI, DNI, DHI, and Tamb
columns_to_plot = ['GHI', 'DNI', 'DHI', 'Tamb']
for column in columns_to_plot:
    data[column].plot(figsize=(12, 6), title=f"Time Series of {column}")
    plt.xlabel("Timestamp")
    plt.ylabel(column)
    plt.show()
