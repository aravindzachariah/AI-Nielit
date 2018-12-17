import tensorflow as tf
u=tf.placeholder(tf.float32)
v=tf.placeholder(tf.float32)
w=tf.placeholder(tf.float32)
sum=tf.add_n([u,v,w])
#tf.assign(u,1.0)
s=tf.Session()
s.run(tf.global_variables_initializer())
o1=s.run(sum,{u:1.0,v:2.0,w:3.0})
print o1
s.close()
