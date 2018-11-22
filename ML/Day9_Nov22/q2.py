import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
import matplotlib.pyplot as plt
data=pd.read_csv("Wine.txt",delimiter="\s+")
print data.head()
data=data.as_matrix()
X=data[:,2:6]
y=data[:,[6]]
r1=KNeighborsRegressor()
r1.fit(X,y)
p1=r1.predict(X)
r2=Lasso()
r2.fit(X,y)
p2=r2.predict(X)
r3=Ridge(0.5)
r3.fit(X,y)
p3=r3.predict(X)
r4=RandomForestRegressor()
r4.fit(X,y)
p4=r4.predict(X)
print "KNN : ",mean_squared_error(y,p1)
print "Lasso : ",mean_squared_error(y,p2)
print "Ridge : ",mean_squared_error(y,p3)
print "Random Forest : ",mean_squared_error(y,p4)
f, axarr = plt.subplots(2,2)
f.suptitle('Different Regression Methods')
axarr[0,0].scatter(y, p1)
axarr[0,0].set_title('KNN')
axarr[0,1].scatter(y, p2)
axarr[0,1].set_title('Lasso')
axarr[1,0].scatter(y, p3)
axarr[1,0].set_title('Ridge')
axarr[1,1].scatter(y, p4)
axarr[1,1].set_title('Random Forest')
plt.show()
