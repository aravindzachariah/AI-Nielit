from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt 
scr=[]
iris =load_iris()
X=iris.data
y=iris.target
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2)
for i in range(1,25):
	knn=KNeighborsClassifier(n_neighbors=i)
	knn.fit(Xtrain,ytrain)
	p=knn.predict(Xtest)
	a=accuracy_score(ytest,p)
	scr.append(a)
plt.plot(range(1,25),scr)
plt.xlabel(" Value of K ")
plt.ylabel("Accuracy Score ")
plt.show()
