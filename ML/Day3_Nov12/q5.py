from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("city.csv")
print data.head()
#print data.shape()
data=data.as_matrix()
X=data[:,1:5]
y=data[:,-1]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
lr=LinearRegression()
lr.fit(X_train,y_train)
p=lr.predict(X_test)
print "Mean Absolute Error",metrics.mean_absolute_error(y_test,p)
print "Mean Squared Error",metrics.mean_squared_error(y_test,p)
print "Root Mean Squared Error",np.sqrt(metrics.mean_squared_error(y_test,p))
print "----------------------"
print "Training Complete     "
print "----------------------"
#n=input("Enter the Brain Weight : ")
#print "The predicted Body weight is :",round(lr.predict(n),2)
plt.scatter(y_test,p)
plt.show()
