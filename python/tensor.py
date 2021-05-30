import pandas as pd
# import tensorflow as tf

# Load dataset.
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')

print(dftrain)

print(dfeval)

y_train = dftrain.loc[ :, ['survived']]
y_eval = dfeval.loc[ :, ['survived']]

y_train

from matplotlib import pyplot as plt
dftrain.age.hist(bins=20)
plt.show()