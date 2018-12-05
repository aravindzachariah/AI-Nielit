#Import required modules
from sklearn.datasets import load_boston
from sklearn.neural_network import MLPRegressor as MLP
from sklearn.metrics import mean_absolute_error,mean_squared_error 
import matplotlib.pyplot as plt

#Load Dataset
data=load_boston()
X=data.data
y=data.target

#Configure Multilayer Perceptron,Train,Predict
mlp=MLP(solver='lbfgs',hidden_layer_sizes=(800),activation='tanh',max_iter=2000,verbose=True)
mlp.fit(X,y)
p=mlp.predict(X)

#Result
print "\n Mean Squared Error : ",mean_squared_error(p,y)
print "\n Mean Absolute Error : ",mean_absolute_error(p,y)
plt.scatter(y,p)
plt.show()

