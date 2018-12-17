import tensorflow as tf
x=tf.fill([2,3],4)
s=tf.Session()
o1=s.run(x)
print o1,
s.close()
