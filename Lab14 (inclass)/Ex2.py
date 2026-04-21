#Create a histogram from the trip miles data
import matplotlib.pyplot as plt
import pandas as pd 

#Read in the data from JSON file
trips_df = pd.read_json("../Trips from area 8.json")
trip_miles_series = trips_df["trip_miles"]

fig= plt.figure()

#Create a histogram of the trip miles data
plt.hist(trip_miles_series)
plt.title ("Distribution of taxi trip miles")
plt.xlabel("Trip miles")
plt.ylabel("Frequency")

plt.show()