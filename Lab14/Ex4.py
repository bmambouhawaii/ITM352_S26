#Create scatter ploy of fares and tips from the file
import json
import matplotlib.pyplot as plt

# Load JSON file
with open("Lab14/Trips_Fri07072017T4 trip_miles gt1.json", "r") as file:
    data = json.load(file)

fares = []
tips = []

# Extract fare and tips
for trip in data:
    fare = trip.get("fare")
    tip = trip.get("tips")

    # Skip missing values
    if fare in (None, "") or tip in (None, ""):
        continue

    try:
        fares.append(float(fare))
        tips.append(float(tip))
    except:
        continue

# Create scatter plot
plt.scatter(fares, tips)

# Labels
plt.xlabel("Fare")
plt.ylabel("Tips")
plt.title("Fare vs Tips")

plt.show()