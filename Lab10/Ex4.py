 # Read a JSON file of taxi trip data and create a dataframe
# Calculate the median fare
import pandas as pd

# Use the correct relative path to the JSON file
taxi_df = pd.read_json("Lab10/Taxi_Trips (1).json")
print(taxi_df.describe())

print (taxi_df.head(8))
median_fare = taxi_df["fare"].median()
print("Median fare amount:", f"${median_fare:.2f}")