from sklearn.datasets import load_boston
from sklearn.neural_network import MLPRegressor as MLP
from sklearn.metrics import mean_absolute_error,mean_squared_error 
data=load_boston()
X=data.data
y=data.target
mlp=MLP(solver='lbfgs',hidden_layer_sizes=(800),activation='tanh',max_iter=800,verbose=True)
mlp.fit(X,y)
p=mlp.predict(X)
print "\n Mean Squared Error : ",mean_squared_error(p,y)
print "\n Mean Absolute Error : ",mean_absolute_error(p,y)

