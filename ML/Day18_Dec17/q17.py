import tensorflow as tf
x=tf.constant([[1,2,3],[4,5,6],[1,2,3]],tf.int32)
y=tf.constant([[3,2,1],[6,5,4],[3,2,1]],tf.int32)
me=tf.multiply(x,5)
s=tf.Session()
o1=s.run(x)
o2=s.run(y)
o3=s.run(me)
print o1,"\n---------\n",o2,"\n----------\n",o3
s.close()
