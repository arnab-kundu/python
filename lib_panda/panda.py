import pandas as pd
df = pd.read_csv('data/survey_results_schema.csv')
print(df)
print(df.shape)
print(df.info())
print(df.head())
print(df.tail())


