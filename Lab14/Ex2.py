import json
import matplotlib.pyplot as plt

# Load the JSON file
with open("Lab14/Trips from area 8.json", "r") as file:
    data = json.load(file)

# Extract trip miles
trip_miles = []

for trip in data:
    if "trip_miles" in trip and trip["trip_miles"] != "":
        trip_miles.append(float(trip["trip_miles"]))

# Create histogram
plt.hist(trip_miles)

# Labels
plt.xlabel("Trip Miles")
plt.ylabel("Frequency")
plt.title("Distribution of Trip Miles")

# Show plot
plt.show()