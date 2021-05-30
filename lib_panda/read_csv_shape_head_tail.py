import pandas as pd

df = pd.read_csv('../csv/survey_results_schema.csv')

print('DataFrame:')
print(df)
print('')

print(df.shape)
#print(df.info())

print('head:')
print(df.head())
print('')

print('tail')
print(df.tail())
print('')

import os
os.system("pause")

