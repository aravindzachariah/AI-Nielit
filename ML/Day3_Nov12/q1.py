
# Question 1
# Develop an ML model for predicting sales for the Advertising data (Advertising.csv file) using Linear Regression.
#Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read Data
Data=pd.read_csv("Advertising.csv")
Data=Data.values
X=Data[:,:-1]
y=Data[:,-1]

#Split Data to training and testing set,Defining Classifier,Fitting and Predicting Data :
X_train,X_test,y_train,y_test=train_test_split(X,y)
lm=LinearRegression()
lm.fit(X_train,y_train)
p=lm.predict(X_test)

#Print Algorithm Performance
print "Mean Absolute Error",metrics.mean_absolute_error(y_test,p)
print "Mean Squared Error",metrics.mean_squared_error(y_test,p)
print "Root Mean Squared Error",np.sqrt(metrics.mean_squared_error(y_test,p))

#Plot Actual Vs Predicted Data
plt.scatter(y_test,p)
plt.show()

