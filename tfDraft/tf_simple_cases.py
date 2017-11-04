import tensorflow as tf
import numpy as np

## test 2d convolution ##
def test_conv2d():
    with tf.Session() as sess:
        input = tf.Variable(tf.ones([1,3,3,1]))
        filter = tf.Variable(tf.ones([3,3,1,1]))
        
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        op = tf.nn.conv2d(input,filter,strides=[1,1,1,1], padding="SAME")
        print sess.run(op)  

## search extremum using gradient descent ##
def test_find_extremum():
    with tf.Session() as sess:
        x = tf.Variable(tf.random_uniform([1,2],-100.0,100.0,dtype=tf.double)) 
        y = tf.matmul(x,x,False,True)
        optim = tf.train.GradientDescentOptimizer(0.1).minimize(y,var_list = x)

        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        for i in xrange(0, 200):
            sess.run(optim)
            print i,":", sess.run([x,y])
 

if __name__ == "__main__":
    test_find_extremum()
