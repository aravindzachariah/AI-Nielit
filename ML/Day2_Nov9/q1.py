# Question 1
# Prepare an ML model using KNN Classifier to predict the Species information for a given iris flower using Sepal Length, Sepal Width, Petal Length & Petal Width. Use the complete iris dataset for training. Use it to predict the species of an iris flower.

# Importing Needed Modules:
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

#Load Iris Dataset
Data=load_iris()
X=Data.data
y=Data.target
tn=Data.target_names

#Defining Classifier,Fitting and Predicting Data :
knn=KNeighborsClassifier()
knn.fit(X,y)
p=knn.predict(X[[1]])

#Print Predicted Vs Actual Result
print " Actual vs Predicted : \n",tn[p]," : ",tn[y[[1]]]

