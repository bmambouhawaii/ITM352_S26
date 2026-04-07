# IMPORT LIBRARIES
# This assignment was completed with assistance from ChatGPT.

import pandas as pd
import time
import os

# Store results for reuse (Requirement #10 support)
results_store = {}

# HELPER FUNCTION: SAVE + EXPORT (Requirement #1)

def save_and_export(result, name):
    # Save result in dictionary
    results_store[name] = result

    # Ask user if they want to export
    choice = input("Export to Excel? (y/n): ").strip().lower() #Removes whitespace (spaces, tabs, new lines) from the beginning and end of a string.

    if choice == 'y': #chat GPT prompt me to install openpyxl.
        filename = input("Enter filename (without .xlsx): ")
        try:
            result.to_excel(f"{filename}.xlsx")
            print("File exported successfully.")
        except Exception as e:
            print("Error exporting file:", e)


# HELPER FUNCTION: CREATE PIVOT (Requirement #9)
# Replace missing values with MEAN instead of 0

def create_pivot(df, values, index, columns=None, aggfunc='sum'):
    pivot = pd.pivot_table(
        df,
        values=values,
        index=index,
        columns=columns,
        aggfunc=aggfunc
    )

    # Replace missing values with column mean
    return pivot.apply(lambda col: col.fillna(col.mean()))

# R1: LOAD DATA

def load_sales_data():
    print("Loading sales data...")
    start_time = time.time()

    try:
        df = pd.read_csv("/Users/beverlymambou/Documents/Github/ITM352_S26/ASSIGNMENTS/sales_data_test.csv")#tried multiple times with URl but did not work, so I downloaded the file and used the local path instead.
    except Exception as e:
        print("Error loading file:", e)
        return None

    end_time = time.time()
    print(f"File loaded successfully in {end_time - start_time:.2f} seconds")

    print("Rows:", len(df))
    print("Columns:", list(df.columns))

    # Replace missing values with 0 (R1 requirement)
    missing_before = df.isna().sum().sum() #Counts the total number of missing values in the DataFrame by summing the count of missing values for each column.
    df = df.fillna(0)#Replaces all missing values in the DataFrame with 0. 
    missing_after = df.isna().sum().sum()

    print("Missing values before:", missing_before)
    print("Missing values after:", missing_after)

    # Create Sales column
    df['Sales'] = df['quantity'] * df['unit_price']

    return df


# MENU FUNCTIONS

# 1. Show first n rows 
def show_first_rows(df):
    total_rows = len(df)

    print(f"\nTotal rows available: {total_rows}")
    print("- Enter a number (e.g., 5)")
    print("- Enter 'all' to display all rows")
    print("- Press Enter to skip")

    choice = input("Your choice: ").strip().lower()

    if choice == "":
        print("Skipping preview.")#If the user presses Enter without typing anything, the function will print "Skipping preview." and then return, effectively skipping the display of any rows.
        return

    elif choice == "all":
        result = df
        print("\nResult:\n", result)

    else:
        try:
            n = int(choice)
            if 1 <= n <= total_rows:
                result = df.head(n)
                print("\nResult:\n", result)
            else:
                print("Number out of range.")
                return
        except ValueError:
            print("Invalid input.")
            return

    save_and_export(result, "first_rows")


# 2. Total sales by region and order type
def total_sales_by_region_order(df):
    print("\nGenerating analysis...\n") #This line prints a message to the console indicating that the analysis is being generated. The "\n" at the beginning and end of the string adds a newline before and after the message for better readability.
    result = create_pivot(df, 'Sales', 'sales_region', 'order_type', 'sum')
    print(result)
    save_and_export(result, "sales_region_order")


# 3. Average sales by region, state, type
def avg_sales_by_region_state(df):
    print("\nGenerating analysis...\n")
    result = create_pivot(df, 'Sales',
                          ['sales_region', 'customer_state'],
                          'order_type', 'mean')
    print(result)
    save_and_export(result, "avg_sales")


# 4. Sales by customer type and order type by state
def sales_by_customer_type(df):
    print("\nGenerating analysis...\n")
    result = create_pivot(df, 'Sales',
                          ['customer_state', 'customer_type'],
                          'order_type', 'sum')
    print(result)
    save_and_export(result, "customer_sales")


# 5. Quantity + Sales by region and product
def sales_region_product(df):
    print("\nGenerating analysis...\n")
    result = pd.pivot_table(
        df,
        values=['quantity', 'Sales'],
        index=['sales_region', 'product_category'],
        aggfunc='sum'#aggregation function that sums the values in the 'quantity' and 'Sales' columns for each combination of 'sales_region' and 'product_category'.
    )

    result = result.apply(lambda col: col.fillna(col.mean()))

    print(result)
    save_and_export(result, "region_product")


# 6. Sales by customer type
def sales_by_customer(df):
    print("\nGenerating analysis...\n")
    result = create_pivot(df, ['quantity', 'Sales'], 'customer_type', None, 'sum')
    print(result)
    save_and_export(result, "customer_totals")


# 7. Max and Min sales by category
def max_min_sales(df):
    print("\nGenerating analysis...\n")
    result = pd.pivot_table(
        df,
        values='Sales',
        index='product_category',
        aggfunc=['max', 'min']
    )

    result = result.apply(lambda col: col.fillna(col.mean()))

    print(result)
    save_and_export(result, "max_min")


# 8. Unique employees by region
def unique_employees(df):
    print("\nGenerating analysis...\n")
    result = df.groupby('sales_region')['employee_name'].nunique()
    print(result)
    save_and_export(result.to_frame(), "unique_employees")


# 9. Custom pivot table (Req #9)
def custom_pivot(df):
    print("\n--- Custom Pivot Table Generator ---")

    # ROWS
    row_options = {"1": "employee_name", "2": "sales_region", "3": "product_category"}
    print("\nSelect rows:")
    for k, v in row_options.items():
        print(f"{k}. {v}") #This loop iterates over the items in the row_options dictionary, printing each key (k) and value (v) in a formatted string. The output will show the available row options for the user to choose from.
    rows = [row_options[c.strip()] for c in input("Choice(s): ").split(",") if c.strip() in row_options]#This line takes the user's input for row choices, splits it by commas, and then creates a list of the corresponding values from the row_options dictionary. It also uses strip() to remove any extra whitespace from the input and checks if the stripped input is a valid key in the row_options dictionary before including it in the final list of rows.

    if not rows:
        print("Invalid row selection.")
        return

    # COLUMNS
    col_options = {"1": "order_type", "2": "customer_type"}
    print("\nSelect columns (optional):")
    for k, v in col_options.items():
        print(f"{k}. {v}")
    col_input = input("Choice(s) or Enter to skip: ").strip() #This line prompts the user to input their choice for columns, allowing them to either select from the provided options or press Enter to skip. The strip() method is used to remove any leading or trailing whitespace from the user's input, ensuring that the input is clean and can be processed correctly in the subsequent code.

    columns = None
    if col_input:
        columns = [col_options[c.strip()] for c in col_input.split(",") if c.strip() in col_options]#This line checks if the user provided any input for columns. If they did, it processes the input similarly to how rows were processed: it splits the input by commas, strips whitespace, and checks if each choice is a valid key in the col_options dictionary before creating a list of column values. If the user pressed Enter without providing input, columns will remain None, which indicates that no column grouping will be applied in the pivot table.

    # VALUES
    val_options = {"1": "quantity", "2": "Sales"}
    print("\nSelect values:")
    for k, v in val_options.items():
        print(f"{k}. {v}")
    values = [val_options[c.strip()] for c in input("Choice(s): ").split(",") if c.strip() in val_options]

    if not values:
        print("Invalid value selection.")
        return

    # AGGREGATION
    agg_options = {"1": "sum", "2": "mean", "3": "count"}
    print("\nSelect aggregation:")
    for k, v in agg_options.items():
        print(f"{k}. {v}")

    agg_choice = input("Choice: ").strip()
    if agg_choice not in agg_options:
        print("Invalid aggregation.")
        return

    # CREATE PIVOT
    print("\nGenerating pivot...\n")
    result = pd.pivot_table(
        df,
        values=values,
        index=rows,
        columns=columns,
        aggfunc=agg_options[agg_choice]
    )

    result = result.apply(lambda col: col.fillna(col.mean())) #This line applies a lambda function to each column of the resulting pivot table. The lambda function takes a column (col) as input and fills any missing values (NaN) in that column with the mean of the column. This is done using the fillna() method, which replaces NaN values with the specified value (in this case, col.mean()). The apply() method applies this operation to each column in the DataFrame, ensuring that all missing values in the pivot table are replaced with their respective column means before the result is printed and exported.
    print(result)

    save_and_export(result, "custom_pivot")


# 10. Exit
def exit_program(df):
    print("Goodbye!")
    exit()


# MENU STRUCTURE
menu= {
    "1": ("Show first n rows", show_first_rows),
    "2": ("Total sales by region and order type", total_sales_by_region_order),
    "3": ("Average sales by region/state/type", avg_sales_by_region_state),
    "4": ("Sales by customer type", sales_by_customer_type),
    "5": ("Sales quantity and price by region/product", sales_region_product),
    "6": ("Sales by customer type totals", sales_by_customer),
    "7": ("Max/min sales by category", max_min_sales),
    "8": ("Unique employees by region", unique_employees),
    "9": ("Custom pivot table", custom_pivot),
    "10": ("Exit", exit_program)
}

# DISPLAY MENU

def display_menu():
    print("\n--- Sales Dashboard ---")
    for key, (desc, _) in menu.items():
        print(f"{key}. {desc}")

# RUN DASHBOARD

def run_dashboard(df):
    while True: #This line starts an infinite loop that will keep the dashboard running until the user chooses to exit. Inside the loop, the menu is displayed, and the user is prompted to make a choice. The loop will continue to run, allowing the user to perform multiple analyses or view different parts of the data, until they select the option to exit the program.
        display_menu()
        choice = input("Choose option: ")

        if choice in menu:
            menu[choice][1](df)
        else:
            print("Invalid choice. Try again.")


# MAIN PROGRAM

data = load_sales_data()

if data is not None:
    run_dashboard(data)