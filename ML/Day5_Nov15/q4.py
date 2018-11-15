from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from  sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
data=pd.read_csv("titanic.csv")
print data.columns
for col in data.columns.values:
	if data[col].dtypes=='object':
		le.fit(data[col].values)
       		data[col]=le.transform(data[col])
print data
data=data.as_matrix()
X=data[:,[0,2,4,5,6,7,8,9,10,11]]
y=data[:,1]
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
