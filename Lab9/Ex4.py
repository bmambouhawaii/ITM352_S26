import csv

filename = "../taxi_1000.csv"

with open(filename, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)

    total_fare = 0.0
    max_distance = 0.0
    count = 0

    for line_num, line in enumerate(csv_reader):

        if line_num == 0:  # header row
            fare_index = line.index("Fare")
            distance_index = line.index("Trip Miles")
        else:
            try:
                tripFare = float(line[fare_index])
                tripDistance = float(line[distance_index])

                if tripFare > 10:   # ONLY fares greater than $10
                    total_fare += tripFare
                    count += 1

                    if tripDistance > max_distance:
                        max_distance = tripDistance

            except (ValueError, IndexError):
                pass

if count > 0:
    average_fare = total_fare / count
    print(f"Total Fare (> $10): {total_fare:.2f}")
    print(f"Average Fare (> $10): {average_fare:.2f}")
    print(f"Max Trip Distance (> $10): {max_distance:.2f}")
else:
    print("No fares greater than $10 found.")