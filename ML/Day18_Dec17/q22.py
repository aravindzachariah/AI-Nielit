import tensorflow as tf
u=tf.placeholder(tf.float32)
#tf.assign(u,1.0)
s=tf.Session()
s.run(tf.global_variables_initializer())
o1=s.run(u,{u:1.0})
print o1
s.close()
