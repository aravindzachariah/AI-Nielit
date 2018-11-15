from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
le=preprocessing.LabelEncoder()
data=pd.read_csv("mining.csv")
print data.head()
for c in data.columns.values:
	if data[c].dtypes=='object':
		le.fit(data[c].values)
		data[c]=le.transform(data[c])
data=data.as_matrix()
X=data[:,1:10]
y=data[:,0]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
knn=KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train,y_train)
yp=knn.predict(X_test)
print accuracy_score(yp,y_test)
print confusion_matrix(yp,y_test)
