import pandas as pd

#Create a DataFrames
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
#
csv_file = 'file.csv'

#
df.to_csv(csv_file, index=False)

print(f"Data written to {csv_file}")