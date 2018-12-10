from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from  sklearn import metrics
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
import numpy as np
data=load_iris()
#print data
#print data.shape()
#data=data.as_matrix()
X=data.data
y=data.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
knn=KNeigbors()
knn.fit(X_train,y_train)
p=knn.predict(X_test)
print "Mean Absolute Error",metrics.mean_absolute_error(y_test,p)
print "Mean Squared Error",metrics.mean_squared_error(y_test,p)
print "Root Mean Squared Error",np.sqrt(metrics.mean_squared_error(y_test,p))
print "----------------------"
print "Training Complete     "
print "----------------------"
plt.scatter(y_test,p)
plt.show()
