people = {
	"first":["Corey", "Jane", "John"],
	"last":["Schafer", "Doe", "Doe"],
	"email":["CoreyMSchafer@gmail.com", "janeDoe@gmail.com", "JohnDoe@email.com"]
}

import pandas as pd

df = pd.DataFrame(people)
print(df)
print('---------------------------------------------------------------------------------')

print(df['last'] == "Doe")
print('---------------------------------------------------------------------------------')

# Crate Filter.Importent note: Filter is a keyword in python. Don't use as variable name.
filt = df['last'] == "Doe"
# Filter without using loc function
print(df[filt])
print('---------------------------------------------------------------------------------')

# Filter using loc function
print(df.loc[filt])
print('---------------------------------------------------------------------------------')

# Get selected column after filtering 
print(df.loc[filt,'email'])
print('---------------------------------------------------------------------------------')

# And & Or oparator in filter
filt = (df['last'] == "Doe") & (df['first'] == "John")
print(filt)
print('---------------------------------------------------------------------------------')
print(df.loc[filt])
print('---------------------------------------------------------------------------------')
filt = (df['last'] == "Schafer") | (df['first'] == "John")
print(df.loc[filt])  
print('---------------------------------------------------------------------------------')
# Alternate value of current filter
print(df.loc[~filt])  


import os
os.system("pause")
