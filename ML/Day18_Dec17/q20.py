import tensorflow as tf
u=tf.Variable(1.0,name="weights")
s=tf.Session()
s.run(tf.global_variables_initializer())
o1=s.run(u)
print o1
s.close()
