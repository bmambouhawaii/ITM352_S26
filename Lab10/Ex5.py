# Read in a CSV file of homes data and create a dataframe
# Do some filtering and statistics on the data
import pandas as pd
import os

# Build the path to the CSV robustly
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "homes_data.csv")
df_homes = pd.read_csv(csv_path)

# Print out the shape of the dataframe and the first few rows.
shape = df_homes.shape
print(f"The homes data has {shape[0]} rows and {shape[1]} columns.")
print(df_homes.head(10))

#Select only the properties with 500 or more units
df_big_properties = df_homes[df_homes["units"] > 500]
df_big_properties = df_big_properties.drop (columns=["id", "easement"])
print(df_big_properties.head(10))

#Convert columns to appropriate data types
df_big_properties["sale_price"] = pd.to_numeric(df_big_properties["sale_price"], errors="coerce")
df_big_properties["land_sqft"] = pd.to_numeric(df_big_properties["land_sqft"], errors="coerce")
df_big_properties["gross_sqft"] = pd.to_numeric(df_big_properties["gross_sqft"], errors="coerce") 

#Drop the rows with missing values in the relevant columns
#df_big_properties = df_big_properties.dropna()

#Drop duplicate rows
df_big_properties = df_big_properties.drop_duplicates()

#Print out the first 10 rows after cleansing
print ("After cleansing the data:") 
print(df_big_properties.head(10))

df_big_properties = df_big_properties[df_big_properties["sale_price"] > 0]
print (df_big_properties.head(10))

#Calculate the average sale price per square foot for the big properties
average_price = df_big_properties["sale_price"].mean()
print(f"The mean sales price for the big properties is ${average_price:.2f}")
