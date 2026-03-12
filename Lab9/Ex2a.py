
import csv
import os

filename = "Lab9/Employee_data.csv - Sheet1.csv"

salaries = []

if os.path.exists(filename):
    
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row
        salary_index = headers.index("Annual_Salary")  # Corrected header name
    print(headers)
    for row in reader:
        print(row)
        # Remove $ and commas, then convert to float
        salary_str = row[salary_index].replace("$", "").replace(",", "")
        try:
            salaries.append(float(salary_str))
        except ValueError:
            pass  # Skip rows with invalid salary

print(salaries)
if salaries:
    average_salary = sum(salaries) / len(salaries)
    print(f"Average Salary: {average_salary:.2f}")
    max_salary = max(salaries)
    print(f"Maximum Salary: {max_salary:.2f}")
    min_salary = min(salaries)
    print(f"Minimum Salary: {min_salary:.2f}")
else:
    print("No salary data found.")

    

