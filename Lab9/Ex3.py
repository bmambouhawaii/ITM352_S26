#read the 1,000
#calculate the total od all fares, average dare, and the max
#trip distance

import csv

# Use the correct relative path from Lab9 to the root
filename = "../taxi_1000.csv"

with open(filename, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)

    total_fare = 0.0
    max_distance = 0.0
    num_rows = 0

    for line in csv_reader:
        if num_rows == 0:  # header row
            try:
                fare_index = line.index("Fare")
                distance_index = line.index("Trip Miles")
            except ValueError:
                raise Exception("Header columns 'Fare' or 'Trip Miles' not found. Check the CSV header.")
        else:
            try:
                tripFare = float(line[fare_index])
                tripDistance = float(line[distance_index])
                total_fare += tripFare
                if tripDistance > max_distance:
                    max_distance = tripDistance
            except (ValueError, IndexError):
                pass  # skip rows with missing or invalid data
        num_rows += 1

    if num_rows > 1:
        average_fare = total_fare / (num_rows - 1)
        print(f"Total fare: {total_fare}")
        print(f"Average fare: {average_fare}")
        print(f"Max trip distance: {max_distance}")
    else:
        print("No data rows found in the CSV file.")

    print(f"Total Fare: {total_fare:.2f}")
    print(f"Average Fare: {average_fare:.2f}")
    print(f"Maximum Distance: {max_distance:.2f}")
