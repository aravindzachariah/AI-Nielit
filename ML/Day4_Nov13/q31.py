from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score
import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
d=pd.read_csv("stair.txt","\s+")
d=d.as_matrix()
X=np.array(zip(d[:,0],d[:,1],d[:,2]))
kmeans=KMeans(n_clusters=5)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)
#plt.scatter(X[:,0],X[:,1],s=50)
#plt.show()
#plt.scatter(X[:,0],X[:,1],s=50,c=y_kmeans,cmap='viridis')
#plt.show()
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.scatter3D(d[:,0],d[:,1],d[:,2],c=y_kmeans,cmap='viridis')
plt.show()
