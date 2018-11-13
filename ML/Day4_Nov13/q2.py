from sklearn.datasets.samples_generator import make_moons
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.cluster import SpectralClustering
X,y_true=make_moons(200,noise=0.05)
kmeans=KMeans(n_clusters=2)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)
plt.scatter(X[:,0],X[:,1],s=50)
plt.show()
plt.scatter(X[:,0],X[:,1],s=50,c=y_kmeans,cmap='viridis')
plt.show()
s=SpectralClustering(2,affinity="nearest_neighbors")
l=s.fit_predict(X)
plt.show()
plt.scatter(X[:,0],X[:,1],s=50,c=l,cmap='viridis')
plt.show()

