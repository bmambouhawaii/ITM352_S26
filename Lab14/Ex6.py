import json
import matplotlib.pyplot as plt

# Load JSON file
with open("Lab14/Trips from area 8.json", "r") as file:
    data = json.load(file)

fares = []
miles = []

# Extract and filter data
for trip in data:
    fare = trip.get("fare")
    trip_miles = trip.get("trip_miles")

    if fare in (None, "") or trip_miles in (None, ""):
        continue

    try:
        fare = float(fare)
        trip_miles = float(trip_miles)
    except:
        continue

    # b. Filter out trips of 0 miles
    if trip_miles == 0:
        continue

    # c. Filter out trips less than 2 miles
    if trip_miles < 2:
        continue

    fares.append(fare)
    miles.append(trip_miles)

# Create scatter plot
plt.scatter(fares, miles, alpha=0.3)

plt.xlabel("Fare")
plt.ylabel("Trip Miles")
plt.title("Fare vs Trip Miles (Filtered)")

# a. Save the plot
plt.savefig("FaresXmiles.png")

plt.show()