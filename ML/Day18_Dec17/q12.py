import tensorflow as tf
x=tf.random_uniform([10,10,3])
y=tf.random_crop(x,[5,5,3])
print x
s=tf.Session()
o1=s.run(x)
o2=s.run(y)
print o1,"\n-----------------------------\n",o2
s.close()
