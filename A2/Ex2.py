#Read a file from URL and save a local CSv file with the first 10 rows



import time


import pandas as pd
import numpy as np
import pyarrow
import os
import gdown



# Google Drive file ID and output filename
gdrive_file_id = "1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
local_filename = "sales_data_test.csv"

pd.set_option("display.max_columns", None)  # Show all columns in the output

def load_csv(filepath):
    print(f"Loading CSV from {filepath}...")
    start_time = time.time()
    try:
        df = pd.read_csv(filepath, engine='python')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded succesfully in {load_time:.2f} seconds.")
        print(f"number of rows: {len(df)}")
        print(f"columns: {df.columns.tolist()}")
        df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d', errors='coerce') # Convert 'order_date' to datetime, coercing errors to NaT
        #df.fillna(0, inplace=True)  # Fill NaN values with 0 for numeric columns
        df['sales'] = df['quantity'] * df['unit_price']  # Create a new 'sales' column by multiplying quantity and unit price
        required_columns = ['quantity', 'unit_price', 'order_date']
        #Check if required columns are present
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing columns in CSV file: {missing_columns}")
        else:
            print("All required columns are present.")
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

# Download the file from Google Drive if it doesn't exist
if not os.path.exists(local_filename):
    print(f"{local_filename} not found. Downloading from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={gdrive_file_id}", local_filename, quiet=False)
else:
    print(f"{local_filename} found locally.")

sales_data = load_csv(local_filename)
if sales_data is not None:
    print(sales_data.head(10))