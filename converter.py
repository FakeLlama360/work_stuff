import pandas as pd


xlms_file = 'Work_stuff/import.xlsm'
df = pd.read_excel(xlms_file)

csv_file = 'Work_stuff/file.csv'
df.to_csv(csv_file, index=False)

print(f"File converted and saved to {csv_file}")
