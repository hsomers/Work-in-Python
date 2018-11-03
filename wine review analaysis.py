# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:06:12 2018

@author: HDSom
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets

# Import the dataframe and clean out any nulls or missing records
df = pd.read_csv('winemag-data-130k-v2.csv')
df = df.dropna()

# Creating a histogram of prices for the wines
x = df['price']
plt.hist(x, bins = 50, range = [0,300])

# Creating a ML algorithm to predict the points of a wine based on its price
df_X = np.array(df.price) # Create an array for price
df_y = np.array(df.points) # Create an array for points

length = len(df_X) # Grab the length of the array so we can reshape it

df_X = df_X.reshape(length, 1) # reshape df_X
df_y = df_y.reshape(length, 1) # reshape df_y

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y,  #split into training and testing data
                                                    test_size=0.33, random_state=42)

reg = LinearRegression() # Create a linear regression model

reg.fit(X_train, y_train) # Fit the model to the data
reg.score(X_train, y_train) # See how well it fits...not so great

pred = reg.predict(X_test) # use reg to predict the points that the test wines got

# Plot the test data with the prediction line
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()