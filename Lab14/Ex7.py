import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load JSON file
with open("Lab14/Trips from area 8.json", "r") as file:
    data = json.load(file)

fares = []
miles = []
dropoffs = []

for trip in data:
    fare = trip.get("fare")
    trip_miles = trip.get("trip_miles")
    dropoff = trip.get("dropoff_community_area")

    if fare in (None, "") or trip_miles in (None, "") or dropoff in (None, ""):
        continue

    try:
        fares.append(float(fare))
        miles.append(float(trip_miles))
        dropoffs.append(int(dropoff))
    except:
        continue

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(fares, miles, dropoffs)

# Labels
ax.set_xlabel("Fare")
ax.set_ylabel("Trip Miles")
ax.set_zlabel("Dropoff Area")

plt.title("3D Plot: Fare vs Miles vs Dropoff Area")

plt.show()