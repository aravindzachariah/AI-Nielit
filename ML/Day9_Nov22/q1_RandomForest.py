from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
data=load_boston()
print data.feature_names
X=data.data
y=data.target
re=RandomForestRegressor()
re.fit(X,y)
p=re.predict(X)
print mean_squared_error(y,p)
plt.scatter(y,p)
plt.show()
