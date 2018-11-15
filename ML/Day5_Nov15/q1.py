from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics as m
import numpy as np
f=pd.read_csv("ex1.txt")
f=f.as_matrix()
profit=f[:,[1]]
pop=f[:,[0]]
plt.scatter(profit,pop)
plt.show()
X_train,X_test,y_train,y_test=train_test_split(pop,profit,test_size=0.2)
lr=LinearRegression()
lr.fit(X_train,y_train)
p=lr.predict(X_test)
print np.sqrt(m.mean_squared_error(y_test,p))
plt.scatter(y_test,p)
plt.show()

