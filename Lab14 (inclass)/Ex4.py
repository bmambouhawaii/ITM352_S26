#Create a catterplot of tips versus fares
import matplotlib.pyplot as plt 
import pandas as pd 

#Read in the data from JSON file
trips_df = pd.read_json("Trips from area 8.json")

fare_series = trips_df["fare"]
tip_series = trips_df["tips"]

fig = plt.figure()

plt.plot(fare_series, tip_series, marker= '.' , linestyle= 'none')
plt.title("Tips vs Fares")
plt.xlabel("Fares in $")
plt.ylabel("Tips in $")
plt.show()
