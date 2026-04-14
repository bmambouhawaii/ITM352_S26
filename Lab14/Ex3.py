#Create a second histogram from the trip miles found in the file

import json
import matplotlib.pyplot as plt

# Load JSON file
with open("Lab14/Trips from area 8.json", "r") as file:
    data = json.load(file)

# Dictionary to store total tips by payment type
tips_by_payment = {}

# Loop through data
for trip in data:
    payment = trip.get("payment_type")
    tip = trip.get("tips")

    # b. Drop rows with NA values
    if payment is None or tip in (None, ""):
        continue

    try:
        tip = float(tip)
    except:
        continue

    # a. Sum tips by payment type
    if payment in tips_by_payment:
        tips_by_payment[payment] += tip
    else:
        tips_by_payment[payment] = tip

# Prepare data for plotting
payment_types = list(tips_by_payment.keys())
total_tips = list(tips_by_payment.values())

# Create bar chart (better than histogram for categories)
plt.bar(payment_types, total_tips)

# c. Labels and title
plt.xlabel("Payment Method")
plt.ylabel("Total Tips")
plt.title("Total Tips by Payment Method")

plt.show()