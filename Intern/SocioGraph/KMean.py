import numpy as np
import random
from sklearn.cluster import AgglomerativeClustering as GMM
import matplotlib.pyplot as plt
products=range(10000)
users=range(1000)
purchases=[]
for p in range(100000):
	u=random.choice(users)
	p=random.choice(products)
	purchases.append((p,u))
#plt.scatter(zip(*purchases)[0],zip(*purchases)[1])
#plt.show()
purchases=np.array(purchases)
gm=GMM(n_clusters=8,linkage='ward')
gm.fit(purchases)
y=gm.fit_predict(purchases)
#zip(*purchases)[1],zip(*purchases)[0]
plt.xlabel("Users")
plt.ylabel("Products")
plt.scatter(purchases[:,1],purchases[:,0],s=50,c=y,cmap='viridis')
plt.show()
