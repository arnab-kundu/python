# Prepare Iris flower dataset
import pandas as pd
from sklearn.datasets import load_iris
data = load_iris()

# prepare dataframe
df = pd.DataFrame(data.data, columns = data.feature_names)

flower_names = []
for i in data.target:
  flower_names.append(data.target_names[i])
df['flower_names'] = flower_names
# df['flower_id'] = data.target
print(df)

# Select column
print(df.loc[:,['flower_names']])

# Select distinct values in a column
import numpy as np
print(np.unique(df.loc[:,['flower_names']]))

# Select 1st row 
print(df.loc[[0], : ])


# Select 1st & 3rd row 
print(df.loc[[0, 2], : ])


# Select 1st to 5th row 
print(df.loc[0:4, : ])

# Select all row 
print(df.loc[ :, : ])
# Select all row 
print(df.loc[0:df.shape[0],:])

# Delete row
deleted_column = df.pop('flower_names')
print(deleted_column)
print(df)

# Insert new row
df['flower_names_new'] = deleted_column
print(df)

# Write data into csv file
df.to_csv('iris_data.csv')

# Read csv data
df = pd.read_csv('iris_data.csv')
print(df)























