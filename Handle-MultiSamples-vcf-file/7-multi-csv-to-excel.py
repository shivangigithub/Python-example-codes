#https://stackoverflow.com/questions/47947639/convert-multiple-csv-files-to-excel-files
import pandas as pd
import os

# Create function that converts csv 2 excel
def csv2excel(filepath, sep=','):
    df = pd.read_csv(filepath, sep=sep)
    newpath = os.path.splitext(filepath)[0] + '.xlsx'
    df.to_excel(newpath, index=False)

# Loop through files and call the function
for f in os.listdir('.'):
    if f.endswith('.csv') and f.startswith('a'):
        csv2excel(f)