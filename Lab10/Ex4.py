 # Read a JSON file of taxi trip data and create a dataframe
# Calculate the median fare
import pandas as pd

# Use the correct relative path to the JSON file
import os

# Try both possible paths for the JSON file
json_paths = ["Taxi_Trips.json", os.path.join("Lab10", "Taxi_Trips.json")]
taxi_df = None
for path in json_paths:
	if os.path.exists(path):
		taxi_df = pd.read_json(path)
		break

if taxi_df is not None:
	print(taxi_df.describe())
	print(taxi_df.head(8))
	if 'fare' in taxi_df.columns:
		print("Median fare:", taxi_df['fare'].median())
	else:
		print("No 'fare' column found")
else:
	print("Taxi_Trips.json file not found in expected locations.")
median_fare = taxi_df["fare_amount"].median()
print("Median fare amount:", f"${median_fare:.2f}")