import json
import matplotlib.pyplot as plt

# Load JSON file
with open("Lab14/Trips from area 8.json", "r") as file:
    data = json.load(file)

fares = []
miles = []

# Extract fare and trip miles
for trip in data:
    fare = trip.get("fare")
    trip_miles = trip.get("trip_miles")

    # Skip missing values
    if fare in (None, "") or trip_miles in (None, ""):
        continue

    try:
        fares.append(float(fare))
        miles.append(float(trip_miles))
    except:
        continue

# a. Scatter plot
plt.scatter(fares, miles, marker="v", color="cyan", alpha=0.2)

plt.xlabel("Fare")
plt.ylabel("Trip Miles")
plt.title("Fare vs Trip Miles")

plt.show()

