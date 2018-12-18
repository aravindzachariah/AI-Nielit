
# # Question 1
# Apply K-Means clustering for the following dataset for two clusters and plot the result.
#    dataset:{2,4,10,12,3,20,30,11,25}

import scipy as sc
import numpy as np
from scipy.cluster.vq import vq
from scipy.cluster.vq import kmeans
import matplotlib.pyplot as plt

dset=np.array([2,4,10,12,3,20,30,11,25])
dset=sc.cast['f'](dset)

cetr1,d1=kmeans(dset,2)
clust1,dist1=vq(dset,cetr1)
clust1

cx=np.arange(1,dset.size+1)
c1=dset[clust1==0]
c2=dset[clust1==1]
plt.scatter(cx[clust1==0],c1,color='r',label="Cluster 1")
plt.scatter(cx[clust1==1],c2,color='b',label="Cluster 2")
plt.legend(loc="best")
plt.show()

