import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) #implicit float32

#now the print

#print(node1, node2)

#Tensor("Const:0", shape = (), dtype = float32)
#Tensor("Const_1:0", shape = (), dtype = float32)

sess = tf.Session()
print(sess.run([node1, node2]))

node3 = tf.add(node1, node2)
print("node3: ", node3)
print("sess.run(node3): ",sess.run(node3))
