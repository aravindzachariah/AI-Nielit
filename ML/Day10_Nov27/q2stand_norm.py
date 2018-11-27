from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
d=pd.read_csv("bank.csv")
d=d.as_matrix()
X=d[:,:20]
y=d[:,-1]
k=KNeighborsClassifier()
"""k.fit(X,y)
p=k.predict(X)
print "Without Scaling ,Accuracy : ",accuracy_score(p,y)"""
X_Scale=preprocessing.scale(X)
k.fit(X_Scale,y)
p=k.predict(X_Scale)
print "After Standardizing, Accuracy : ",accuracy_score(p,y)
X_Norm=preprocessing.normalize(X)
k.fit(X_Norm,y)
p=k.predict(X_Norm)
print "After Standardizing, Accuracy : ",accuracy_score(p,y)

