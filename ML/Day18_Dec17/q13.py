import tensorflow as tf
x=tf.constant([[-1,-2,-3],[0,1,2]],tf.int32)
y=tf.zeros_like(x,tf.int32)
z=tf.not_equal(x,y)
s=tf.Session()
o1=s.run(x)
o2=s.run(y)
o3=s.run(z)
print o1,"\n-----------\n",o2,"\n------------\n",o3
s.close()
