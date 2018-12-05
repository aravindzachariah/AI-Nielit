from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt

train1=pd.read_csv("/home/ai7/Desktop/common/ML/Day2/Questions/Immunotherapy.csv", delimiter=",")
test1=pd.read_csv("/home/ai7/Desktop/common/ML/Day2/Questions/Immunotherapy.csv", delimiter=",")
print(train1)
print(test1)

X_train,X_test,y_train,y_test=train_test_split(train1,test1)

train=train1.as_matrix()
test=test1.as_matrix()
print(train.shape)
print(test.shape)

iknn=KNeighborsClassifier(n_neighbors=1)
iknn.fit(train [:,0:6], train[:,7])
p=iknn.predict(test [:,0:6])
print(p)
print(confusion_matrix(test[:,7],p))
print("Accuracy_score is: ", accuracy_score(test[:,7],p))
score=list()
for i in range(1,25):
  iknn=KNeighborsClassifier(n_neighbors=i)
  iknn.fit(train [:,0:6], train[:,7])
  p=iknn.predict(test [:,0:6])
  a=accuracy_score(test[:,7],p)
  score.append(a)
  

plt.plot(range(1,25),score)
plt.xlabel("Value of k ")
plt.ylabel("Accuracy_score")
plt.show()