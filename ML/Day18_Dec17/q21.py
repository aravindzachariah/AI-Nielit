import tensorflow as tf
u=tf.Variable(1.0,name="weights")
v=tf.Variable(2.0,name="weights")
w=tf.Variable(3.0,name="weights")
sum=tf.add(u,tf.add(v,w))
s=tf.Session()
s.run(tf.global_variables_initializer())
o1=s.run(u)
o2=s.run(v)
o3=s.run(w)
o4=s.run(sum)
print o1,"+",o2,"+",o3,"=",o4
s.close()
