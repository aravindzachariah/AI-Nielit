from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics as m
import numpy as np
from mpl_toolkits import mplot3d
from sklearn.model_selection import train_test_split
f=pd.read_csv("ex2.txt")
f=f.as_matrix()
Hsize=f[:,[0]]
Hno=f[:,[1]]
Hprice=f[:,[2]]
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.scatter3D(Hsize,Hno,Hprice)
plt.show()
lr=LinearRegression()
X=f[:,[0,1]]
y=f[:,[2]]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
lr.fit(X_train,y_train)
yp=lr.predict(X_test)
print np.sqrt(m.mean_squared_error(y_test,yp))


