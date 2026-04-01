#Read a csv file and create a dataframe
#Pivot the dataframe, aggregating sales by region, with columns defined by order_type and totals.

import pandas as pd
import numpy as np
import pyarrow

filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option("display.max_columns", None)  # Show all columns in the output

try:
    df = pd.read_csv(
        filename,
        engine='pyarrow',
        dtype_backend="pyarrow",
        parse_dates=['order_date'],
        on_bad_lines='skip'
    )
except Exception as e:
    print(f"Error reading CSV: {e}")
    df = pd.DataFrame()

if not df.empty:
    # Coerce to numeric to ensure calculations are correct
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
    df['sales'] = df['quantity'] * df['unit_price']

    # Create pivot table with numpy sum, margins for totals
    pivot_table = df.pivot_table(
        index='sales_region',
        columns='order_type',
        values='sales',
        aggfunc=np.sum,
        margins=True,
        margins_name='Total Sales'
    )
    print(pivot_table)
else:
    print("No data to display.")