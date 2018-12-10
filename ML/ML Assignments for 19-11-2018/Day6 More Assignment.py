#1) The data (bank.csv) is related to direct marketing campaigns
# (phone calls) of a Portuguese banking institution. Develop a
# suitable ML model for classification. The classification goal is to
# predict if the client will subscribe a term deposit. Develop models
# using knn, svm, nb and logistic regression. Observe the accuracy
# obtained by different models. Also study the precision, recall , F1
# score parameters. Find out which algorithm is most suitable

#Import Modules
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics  import mean_squared_error
from sklearn.svm import SVR

bank = pd.read_csv('bank.csv')
print bank.head()

# 2) The data (bikerentals.txt) is related to a bike rental company.
# Develop a suitable ML model for predicting the number of bikes
# rented (The last column of the data) daily.
# (Source of data: https://github.com/mhyhre/mlcourse_open/blob/master/data/bikes_rent.csv)

#Read Data
bike_data = pd.read_csv("https://raw.githubusercontent.com/mhyhre/mlcourse_open/master/data/bikes_rent.csv")
print bike_data.head()
print bike_data.shape
bike_data = bike_data.as_matrix()
X = bike_data[:,:12]
y = bike_data[:,12]

reg_model = LinearRegression()
reg_model.fit(X,y)
p = reg_model.predict(X)
plt.scatter(p,y)
plt.show
print "RMSE LRG: ",mean_squared_error(y,p)**0.5

reg_model2 = SVR()
reg_model2.fit(X,y)
p2 = reg_model2.predict(X)
plt.scatter(p2,y)
plt.show
print "RMSE SVR: ",mean_squared_error(y,p2)**0.5

