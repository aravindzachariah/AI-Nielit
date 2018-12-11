
# coding: utf-8

# # Question 2

# 2.Create a plot with different linestyle,color and marker for ,say, numbers less than 
#            50 and greater than or equal to 50 for an array of 10 random integers between 1 and 100
# 		
# 		steps
# 		1. import pyplot and numpy
# 		2. create figure 
# 		3. add a subplot
# 		4. create and store 10 random integers between 1 and 100 in y array
# 		5. split the array into two y1 and y2. hint:less than 50 in y1 ,others in y2,boolen indexing 
# 		6. store last element of y1 as first in y2: hint numpy.insert(array,index,value)
# 		7. create 10 even numbers in x array hint arange
# 		7. call plot of step3 return value by supplying x array containg index values 0 thru size of y1
# 		8. again call plot of step3 return value by supplying the required values
# 		9. show the figure

# In[7]:


import matplotlib.pyplot as plt
import numpy as np
import random


# In[6]:


fig=plt.figure(figsize=(8,8))
sub1=fig.add_subplot(2,2,1)


# In[33]:


y=[]
for j in range(10): 
        y.append(random.randint(1, 100)) 
y=np.array(y)
y1=y[y<50]
y2=y[y>=50]
print y1,y2,"\n"
y2=np.insert(y2,0,y1[-1])
print y2,"\n"
x=np.arange(2,22,2)
print x,"\n"


# In[50]:


sub1.plot(x[:y1.size],y1)
fig.show()

