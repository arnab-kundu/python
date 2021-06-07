import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression

# data = pd.read_csv('data.csv')  # load data set
xyData = {
    "x": [-1, 0, 1, 2, 3, 4],
    "y" : [-3, -1, 1, 3, 5, 7]
}
data = pd.DataFrame(xyData)

X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions
print(linear_regressor.predict([[5]]))




#############
# seaborn
#############

import seaborn as sns  # To visualize
import matplotlib.pyplot as plt
# seaborn version
print(sns.__version__)

# scatter plot
sns.scatterplot(data=data, x=None, y=None)

# line plot
sns.lineplot(data=data, x=None, y=None)
plt.show()

import os
os.system('pause')