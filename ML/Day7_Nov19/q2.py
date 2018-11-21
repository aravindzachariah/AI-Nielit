import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import accuracy_score,mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv('bikerental.txt',delim_whitespace=True)
data.head()
data.dropna(inplace=True)
X = data.drop('cnt',axis=1)
y = data['cnt']
X_train,X_test,y_train,y_test = train_test_split(X,y)
model = SVR()
lmodel = LinearRegression()
model.fit(X_train,y_train)
lmodel.fit(X_train,y_train)
models= [model,lmodel]
for i in models:
    print "\n",i
    pred = i.predict(X_test)
    print "MSE: ",mean_squared_error(y_test,pred),"\n"

