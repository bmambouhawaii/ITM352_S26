#Read a csv file and create a dataframe
#Pivot the dataframe, aggregating sales by region, with columns defined by order_type and totals.

import pandas as pd
import numpy as np
import pyarrow

filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option("display.max_columns", None)  # Show all columns in the output
pd.set_option("display.float_format", '{:,.2f}'.format)  # Format floats to 2 decimal places

df = pd.read_csv(filename, engine='pyarrow')
df['order_date'] = pd.to_datetime(df['order_date'],format='%Y-%m-%d', errors='coerce') # Convert 'order_date' to datetime, coercing errors to NaT

#Coerce quantity and unit_price to numeric, coercing errors to NaN (not a number)
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['sales'] = df['quantity'] * df['unit_price'] # Create a new 'sales' column by multiplying quantity and unit price

#Support common state column names in class datasets
state_col = 'customer_state'

# Format floats to 2 decimal places
pd.set_option("display.float_format", "{:,.2f}".format)

pivot_table = pd.pivot_table(df,
                                values='sales',
                                index= "customer_state",  # Use 'customer_state' as the index for the pivot table
                                columns =['customer_type', 'order_type'],  # Create columns based on 'customer_type' and 'order_type'
                                aggfunc=np.sum,  # Aggregate sales using the sum function
                                fill_value=0,  # Fill missing values with 0
                                margins=True,  # Add a total row and column
                                margins_name='Total Sales')


print(pivot_table)