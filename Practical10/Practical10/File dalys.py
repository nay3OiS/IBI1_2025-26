import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/users/11467/downloads")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())
first_10 = dalys_data.iloc[0:10,2:4]
print("First 10 line of year and DALYs:", first_10)
# Create a Boolean that is True when the “Entity” is “Zimbabwe”, but false otherwise
zimbabwe = dalys_data.loc[dalys_data["Entity"]=="Zimbabwe",["Year","DALYs"]]
print("The record year of zimbabwe:", zimbabwe)
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
# Find the largest/smallest DALYs countries in 2019
max_dalys_2019 = recent_data.loc[recent_data["DALYs"].idxmax()]
min_dalys_2019 = recent_data.loc[recent_data["DALYs"].idxmin()]
print("The country that has max DALYs in 2019:", max_dalys_2019["Entity"])
print("The country that has min DALYs in 2019:", min_dalys_2019["Entity"])
max_country = max_dalys_2019["Entity"]
max_country_data = dalys_data.loc[dalys_data["Entity"] == max_country, :]
# Plot the trend of DALYs for the country with the largest DALYs in 2019
plt.figure(figsize=(10, 5))
plt.plot(max_country_data.Year, max_country_data.DALYs, 'r-o', label=max_country)
plt.xlabel("Year")
plt.ylabel("DALYs (Disability Adjusted Life Years)")
plt.title(f"DALYs Trend in {max_country} (1990-2019)")
plt.xticks(max_country_data.Year, rotation=-90)
plt.legend()
plt.tight_layout()
plt.show()
# What was the distribution of DALYs across all countries in 2019?
dalys_2019 = recent_data["DALYs"]
plt.figure(figsize=(10, 5))
plt.hist(dalys_2019, bins=30, color='skyblue', edgecolor='black')
plt.xlabel("DALYs Value")
plt.ylabel("Number of Countries")
plt.title("Distribution of DALYs Across All Countries in 2019")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


