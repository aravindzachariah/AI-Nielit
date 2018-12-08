# Question 2
# Print the Accuracy Score and Confusion matrix for KNN Classifier using iris data. (Split iris dataset to train and test sets.)

# Importing Needed Modules:
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix

# Load Iris Dataset
Data=load_iris()
X=Data.data
y=Data.target

#Split Data to training and testing set,Defining Classifier,Fitting and Predicting Data :
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
knn=KNeighborsClassifier()
knn.fit(X_train,y_train)
p=knn.predict(X_test)

#Print Confusion Matrix and Accuracy
print "Accuracy Score : ",accuracy_score(p,y_test)
print "\nConfusion Matrix: \n",confusion_matrix(p,y_test)

