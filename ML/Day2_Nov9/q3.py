# # Question 3

# The dataset (Immunotherapy.csv) contains information about wart treatment results of 90 patients using immunotherapy. Develop a KNN Classifier to predict the success of the treatment. Print confusion matrix. Also plot the graph showing the variation of accuracy score for the different values of k.

# Importing Needed Modules:
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
import matplotlib.pyplot as plt

# Read the csv file
Data=pd.read_csv("Immunotherapy.csv")

#Split Data to Data and Target 
Data=Data.values             #Convert DataFrame to array
X=Data[:,:-1]
y=Data[:,-1]

#Split Data to training and testing set,Defining Classifier,Fitting and Predicting Data :
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
knn=KNeighborsClassifier()
knn.fit(X_train,y_train)
p=knn.predict(X_test)

#Print Confusion Matrix and Accuracy
print "Confusion Matrix : \n ",confusion_matrix(p,y_test)
print "Accuracy Score : \n ",accuracy_score(p,y_test)

#Train the algorithm for different number of neighbors and compute accuracy score
s=[]
for i in range(1,26):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    p=knn.predict(X_test)
    acs=accuracy_score(p,y_test)
    s.append(acs)

#Plot Neighbor Numbers Vs Accuracy Score
plt.plot(range(1,26),s)
plt.title('Number of Neighbors Vs Accuracy Score ')
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy Score')
plt.show()

