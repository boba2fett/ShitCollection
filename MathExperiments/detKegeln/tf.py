from __future__ import absolute_import, division, print_function, unicode_literals
import os

import tensorflow as tf

import cProfile
import numpy as np
import random
import matplotlib.pyplot as plt

inputs1 = tf.placeholder(shape=[3,3],dtype=tf.float32)
W = tf.Variable(tf.random_uniform(shape=[1],minval=0,maxval=9,dtype=tf.int8))
Qout = tf.matmul(inputs1,W)
predict = tf.argmax(Qout,1)


nextQ = tf.placeholder(shape=[1,4],dtype=tf.float32)
loss = tf.reduce_sum(tf.square(nextQ - Qout))
trainer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
updateModel = trainer.minimize(loss)

y = .99
e = 0.1
num_episodes = 2000
#create lists to contain total rewards and steps per episode
jList = []
rList = []

for i in range(num_episodes):
    a,allQ = [predict,Qout],feed_dict={inputs1:np.identity(16)[s:s+1]}
    if np.random.rand(1) < e:
        a[0] = env.action_space.sample()
    #Get new state and reward from environment
    s1,r,d,_ = env.step(a[0])
    #Obtain the Q' values by feeding the new state through our network
    Q1 = Qout,feed_dict={inputs1:np.identity(16)[s1:s1+1]}
    #Obtain maxQ' and set our target value for chosen action.
    maxQ1 = np.max(Q1)
    targetQ = allQ
    targetQ[0,a[0]] = r + y*maxQ1
    #Train our network using target and predicted Q values
    _,W1 = [updateModel,W],feed_dict={inputs1:np.identity(16)[s:s+1],nextQ:targetQ}
    s = s1




varM=tf.Variable(initial_value=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],shape=[3,3],dtype=tf.float32)
conM=tf.constant([[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],shape=[3,3],dtype=tf.float32)
conM=tf.constant([[9,9,9],[0,9,9],[9,0,9]],shape=[3,3],dtype=tf.float32)
print(tf.linalg.det(varM).numpy())
print(tf.linalg.det(conM).numpy())