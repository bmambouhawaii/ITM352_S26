#Read a file from URL and save a local CSv file with the first 10 rows


import pandas as pd
import numpy as np
import pyarrow


filename = "https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA/view"

df = pd.read_csv(filename, engine='pyarrow')

outfile= "sales_data_test.csv"

df.head(10).to_csv(outfile, index=False)