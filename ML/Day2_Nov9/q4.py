# Question 4
# Identify a suitable dataset from your area of interest for a classification problem (Should not be the same as Day1 solution). Develop an ML model to do prediction. Print confusion matrix and accuracy score.

# Data Information
# Source:
# Owner of database: Volker Lohweg (University of Applied Sciences, Ostwestfalen-Lippe, volker.lohweg '@' hs-owl.de) 
# Donor of database: Helene  (University of Applied Sciences, Ostwestfalen-Lippe, helene.doerksen '@' hs-owl.de) 
# Date received: August, 2012  
# Data Set Information:
# Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

# Attribute Information:
# 1. variance of Wavelet Transformed image (continuous) 
# 2. skewness of Wavelet Transformed image (continuous) 
# 3. curtosis of Wavelet Transformed image (continuous) 
# 4. entropy of image (continuous) 
# 5. class (integer) 
 
# Sample Real Currency: -1.3971,3.3191,-1.3927,-1.9948
# Sample CounterFit Currency: 2.2504,3.5757,0.35273,0.2836

# Importing Needed Modules:
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd

# Read the csv file
t1=pd.read_csv("data_banknote_authentication.txt")
t=t1.values
X=t[:,:-1]
y=t[:,4]

#Split Data to training and testing set,Defining Classifier,Fitting and Predicting Data :
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2)
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(Xtrain,ytrain)
p=knn.predict(Xtest)

#Print Confusion Matrix and Accuracy
print "Accuracy Score :",accuracy_score(ytest,p)
print "Confusion Matrix : \n",confusion_matrix(ytest,p)

#Function returns Counterfit/Not
def fn(p):
	if p==0:
		return "Counterfit"
	else:
		return "Not Counter Fit"
			
#Input Data and print test results
a1=[]
a=input("Enter Variance,Skewness,Curtosis,Entropy of Wavlet Transform Image : ")
a1.append(a)
print fn(knn.predict(a1))

