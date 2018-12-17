import tensorflow as tf
x=tf.constant([[1,2],[3,4],[5,6]],tf.int32)
y=tf.random_shuffle(x)
s=tf.Session()
o1=s.run(x)
o2=s.run(y)
print o1,"\n",o2
s.close()
