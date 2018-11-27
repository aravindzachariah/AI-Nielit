from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import classification_report
from sklearn import preprocessing
d=pd.read_csv("Immunotherapy.csv")
d=d.as_matrix()
X=d[:,:-7]
y=d[:,7]
k=KNeighborsClassifier()
k.fit(X,y)
p=k.predict(X)
print "Without Scaling ,Accuracy : \n",classification_report(p,y)
X_Scale=preprocessing.scale(X)
k.fit(X_Scale,y)
p1=k.predict(X_Scale)
print "After Standardizing, Accuracy : \n",classification_report(p1,y)
min_max_scaler = preprocessing.MinMaxScaler()
X_Norm = min_max_scaler.fit_transform(X)
#X_Norm=preprocessing.normalize(X)
k.fit(X_Norm,y)
p2=k.predict(X_Norm)
print "After Standardizing, Accuracy : \n",classification_report(p2,y)

