import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("Lab14/taxi trips Fri 7_7_2017.csv")

# Create pivot table
heatmap_data = df.pivot_table(
    index="pickup_community_area",
    columns="dropoff_community_area",
    aggfunc="size",
    fill_value=0
)

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data)

plt.title("Heatmap of Pickup vs Dropoff Areas")
plt.xlabel("Dropoff Area")
plt.ylabel("Pickup Area")

plt.show()