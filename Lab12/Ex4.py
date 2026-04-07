#Get public license data from the City of Chicago's Data Portal

import pandas as pd
from sodapy import Socrata

#Create a Sodapy client to access the City of Chicago's Data Portal
client = Socrata("data.cityofchicago.org", None) #socrata is going to do the data capture for us.

#specify the JSON file for license data
json_file = "rr23-ymwb"

results = client.get (json_file, limit=500)
#Convert the results to a DataFrame for easier analysis
df = pd.DataFrame.from_dict(results)

print (df.head())

vehicles_and_fuel_sources = df[["public_vehicle_number", "vehicle_fuel_source"]]
print ("Public Vehicle Number and Fuel Source:")
print(vehicles_and_fuel_sources.head())

vehicles_by_fuel_source = vehicles_and_fuel_sources.groupby("vehicle_fuel_source").count()
print ("Number of public vehicles by Fuel Source:")
print(vehicles_by_fuel_source)