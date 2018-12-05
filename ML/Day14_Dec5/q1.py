#Import packages
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

#Load Iris Data
iris = load_iris()
X=iris.data
y=iris.target

#Define Classifier and Parameters,activation function set to 'relu'
mlp=MLPClassifier(activation='relu',hidden_layer_sizes=(200),max_iter=500,solver="lbfgs")

#Fit Data to Classifier
mlp.fit(X,y)

#Predict Data
p=mlp.predict(X)

#Print Confusion Matrix
print"Activation 'relu': \n",(confusion_matrix(y,p))

#Define Classifier and Parameters,activation function set to 'tanh'
mlp1=MLPClassifier(activation='tanh',hidden_layer_sizes=(200),max_iter=500,solver='lbfgs')

#Fit Data to Classifier
mlp1.fit(X,y)

#Predict Data
p=mlp1.predict(X)

#Print Confusion Matrix
print"\nActivation 'tanh': \n",(confusion_matrix(y,p))

#Define Classifier and Parameters,activation function set to 'identity'
mlp2=MLPClassifier(activation='identity',hidden_layer_sizes=(300),max_iter=1000,solver='lbfgs')

#Fit Data to Classifier
mlp2.fit(X,y)

#Predict Data
p=mlp2.predict(X)

#Print Confusion Matrix
print"\nActivation 'identity': \n",(confusion_matrix(y,p))

#Define Classifier and Parameters,activation function set to 'logistic'
mlp3=MLPClassifier(activation='logistic',hidden_layer_sizes=(200),max_iter=500,solver='lbfgs')

#Fit Data to Classifier
mlp3.fit(X,y)

#Predict Data
p=mlp3.predict(X)

#Print Confusion Matrix
print"\nActivation 'logistic': \n",(confusion_matrix(y,p))

