import pandas as pd


#Create a DataFrames
data ={
    'number' :[1],
    'stock' :[20],
    'name' :['NSP-STICK'],
    'id_num' :[23121],
    'price' :[20],
    'type' :['kč'],
    'kategory' :['Electronicks']
}

df = pd.DataFrame(data)

#Specify the path for the CSV file
csv_file = 'file.csv'

#Write the DataFrame o a CSV file
df.to_csv(csv_file, index=False)

print(f"Data written to {csv_file}")