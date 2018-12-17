import tensorflow as tf
x=tf.random_normal([3,2],stddev=2)
print x
s=tf.Session()
o=s.run(x)
print o
s.close()
