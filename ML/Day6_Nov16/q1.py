#Import Required Modules

import  matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix

#Load Numeric digit image data from sklearn

data=load_digits()  
X=data.images
y=data.target
ilabels=list(zip(X,y))

#Print the images and thier label

for index,(image,label) in enumerate(ilabels[:8]):
	plt.subplot(1,8,index+1)
	plt.axis('off')
	plt.imshow(image,cmap='inferno',interpolation='nearest')
	plt.title(label)
plt.show()

#Reshaping the (8X8) N image to 64  N images

n=len(X)
X=X.reshape(n,-1)

#Split Train Data and test Data

X_train=X[:n//2]
y_train=y[:n//2]
X_test=X[n//2:]
y_test=y[n//2:]

#Model Training and Prediction

model=SVC(gamma=0.001)
model.fit(X_train,y_train)
p=model.predict(X_test)

#Performance of Model

c=classification_report(y_test,p)
print(confusion_matrix(y_test,p))
print(c)

