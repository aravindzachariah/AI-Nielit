import tensorflow as tf
x=tf.constant([[1,2,3],[4,5,6],[1,2,3]],tf.int32,name="Tensor1")
y=tf.constant([[3,2,1],[6,5,4],[3,2,1]],tf.int32,name="Tensor2")
z=tf.constant([[1,1,1],[2,2,2],[3,3,3]],tf.int32,name="Tensor3")
sum=tf.add(tf.add(x,y),z)
s=tf.Session()
o1=s.run(x)
o2=s.run(y)
o3=s.run(z)
o4=s.run(sum)
tf.summary.FileWriter('./tb1',s.graph)
print o1,"\n---------\n",o2,"\n----------\n",o3,"\n----------\n",o4
s.close()
