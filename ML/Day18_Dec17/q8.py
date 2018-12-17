import tensorflow as tf
x=tf.linspace(5.0,10.0,50)
print x
s=tf.Session()
o=s.run(x)
print o
s.close()
