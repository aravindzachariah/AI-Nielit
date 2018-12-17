import tensorflow as tf
x=tf.constant([[1,3,5],[4,6,8]],tf.int32)
s=tf.Session()
o1=s.run(x)
print o1
s.close()
