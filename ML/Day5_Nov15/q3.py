from sklearn.linear_model import LogisticRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics as m
import numpy as np
from mpl_toolkits import mplot3d
f=pd.read_csv("ex3.txt")
f=f.as_matrix()
X_train,X_test,y_train,y_test=train_test_split(f[:,[0,1]],f[:,2],test_size=0.2)
lr=LogisticRegression()
lr.fit(X_train,y_train)
p=lr.predict(X_test)
print np.sqrt(m.mean_squared_error(y_test,p))
yp=lr.predict(X_test)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.scatter3D(X_test[:,0],X_test[:,1],yp,c=yp,cmap='RdYlBu')
ax.set_xlabel('Score Exam 1')
ax.set_ylabel('Score Exam 2')
ax.set_zlabel('Selected/Not Selected \n(Blue/Red)')
plt.show()


