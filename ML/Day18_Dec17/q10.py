import tensorflow as tf
x=tf.random_uniform([3,2],minval=0,maxval=2)
print x
s=tf.Session()
o=s.run(x)
print o
s.close()
