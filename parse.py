import pandas as pd
import json
import os

path = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/University /Año 2 Esic/Aldea global 2/Diagnóstico P-I.xlsx")
try:
    xl = pd.ExcelFile(path)
    print("Sheets:", xl.sheet_names)
    for sheet in xl.sheet_names:
        print(f"\n======== SHEET: {sheet} ========")
        df = xl.parse(sheet)
        print(df.head(25))
except Exception as e:
    print(f"Error parsing excel: {e}")
