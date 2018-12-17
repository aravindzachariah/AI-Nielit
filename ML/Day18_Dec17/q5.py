import tensorflow as tf
x=tf.fill([3,2],5)
s=tf.Session()
o1=s.run(x)
print o1,
s.close()
