import os  
import pandas as pd  
import matplotlib.pyplot as plt 
import numpy as np

os.chdir("\Users\11467\Desktop\IBI\IBI1_2025-26\resit\practical10")

# Check current working directory and list files inside the folder
print("Current working directory:", os.getcwd())
print("Files in working directory:", os.listdir())

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Display first 5 rows
print("First 5 rows of the dataset")
print(dalys_data.head(5))

# Print basic metadata of the dataframe
print("Dataset basic information")
dalys_data.info()

# Print statistical summary for all numeric columns
print("Statistical summary")
print(dalys_data.describe())

# Extract global min/max DALY values and earliest/latest recorded years
max_daly = dalys_data["DALYs"].max()
min_daly = dalys_data["DALYs"].min()
first_year = dalys_data["Year"].min()
last_year = dalys_data["Year"].max()
print(f"Maximum DALY value across all records: {max_daly}")
print(f"Minimum DALY value across all records: {min_daly}")
print(f"Earliest year recorded in dataset: {first_year}")
print(f"Most recent year recorded in dataset: {last_year}")

# Extract rows 100 to 110 and display all columns for this range
rows_100_110 = dalys_data.iloc[100:111, :]
print("Rows 100 to 110 (all 4 columns)")
print(rows_100_110)

# Extract country name for this row range (all rows belong to one single country)
target_country = rows_100_110["Entity"].unique()[0]
# Find the row with maximum DALY value within this range
max_daly_subset = rows_100_110.loc[rows_100_110["DALYs"] == rows_100_110["DALYs"].max()]
year_max_daly = max_daly_subset["Year"].values[0]
print(f"[Comment] Country in rows 100-110: {target_country}")
print(f"[Comment] Year with the highest DALY value in this range: {year_max_daly}")

# Create boolean mask: True if DALYs < 17000, False otherwise
low_daly_mask = dalys_data["DALYs"] < 17000
# Filter full dataset using the boolean mask
low_daly_records = dalys_data.loc[low_daly_mask, :]
print("All records with DALYs less than 17000")
print(low_daly_records)

# Show unique countries that have at least one year with DALYs < 17000
unique_low_daly_countries = low_daly_records["Entity"].unique()
print("List of countries with at least one year DALYs < 17000:")
print(unique_low_daly_countries)

# Subset data only for China, retain DALYs and Year columns
china_data = dalys_data.loc[dalys_data.Entity == "China", ["DALYs", "Year"]]

# Plot DALY over time for China
plt.plot(china_data.Year, china_data.DALYs, 'b+')

# Rotate x-axis year labels
plt.xticks(china_data.Year, rotation=-90)

# Add clear plot labels and show the plot
plt.title("DALY Rates Over Time in China")
plt.xlabel("Year")
plt.ylabel("Total DALYs")
plt.show()

# To answer the question stated in file questions.txt
# Create boolean mask to filter rows where DALYs exceed 100000
high_daly_mask = dalys_data[dalys_data["DALYs"] > 100000]
high_daly_records = dalys_data.loc[high_daly_mask, :]
print("Records with DALYs greater than 100000")
print(high_daly_records)

# Extract unique country names that meet the condition
high_daly_countries = high_daly_records["Entity"].unique()
print("Countries that have recorded DALYs > 100000 in at least one year:")
print(high_daly_countries)