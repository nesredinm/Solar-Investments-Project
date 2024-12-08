import pandas as pd

#load the data set
data = pd.read_csv("D:/AI Mastery/data/benin-malanville.csv")


#Display basic info
print (data.info())
print (data.head())

# Generate summary statistics for numeric columns
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
