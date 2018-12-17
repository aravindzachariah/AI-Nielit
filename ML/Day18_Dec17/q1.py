import tensorflow as tf
x=tf.zeros([2,3],tf.int32)
print x
s=tf.Session()
o=s.run(x)
print o
s.close()
