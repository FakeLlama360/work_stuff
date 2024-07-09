import pandas as pd


xlms_file = 'Home(H:)/Samuel_Mlýnek/Programing/work_stuff/bulk-import_v5.1_cs.xlsm'
df = pd.read_excel(xlms_file, engine='openpyxl')

csv_file = 'Home(H:)/Samuel_Mlýnek/Programing/work_stuff'
df.to_csv(csv_file, index=False)

print(f"File converted and saved to {csv_file}")
