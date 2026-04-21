#Create a scatterplot of fares by trip miles
import matplotlib.pyplot as plt 
import pandas as pd 

#Read in the data from JSON file
trips_df = pd.read_json("Trips from area 8.json")

trip_miles_gt_0 = trips_df[["trip_miles","fare"]].query('trip_miles > 0') #I only want to include trips with miles greater than 0 in the dataframe.
fare_series = trip_miles_gt_0["fare"]
trip_series = trip_miles_gt_0["trip_miles"]

fig = plt.figure()

plt.plot(trip_series, fare_series, linestyle= 'none', marker= 'v', color= 'c', alpha=0.2)
plt.title("Fares by Taxi Trip Miles")
plt.xlabel("Trip Miles")
plt.ylabel("Fares in $")
plt.show()