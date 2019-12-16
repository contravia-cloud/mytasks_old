#!/usr/bin/env python
# coding: utf-8

# **[MSL-01]** 필요한 모듈을 임포트하고 난수의 시드를 설정한다.

# In[1]:


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

np.random.seed(20160612)
tf.set_random_seed(20160612)


# **[MSL-02]** MNIST 데이터 세트를 준비한다.

# In[2]:


mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)


# **[MSL-03]** 단층 신경망를 이용한 확률 p의 계산식을 준비한다.

# In[3]:


num_units = 1024

x = tf.placeholder(tf.float32, [None, 784])

w1 = tf.Variable(tf.truncated_normal([784, num_units]))
b1 = tf.Variable(tf.zeros([num_units]))
hidden1 = tf.nn.relu(tf.matmul(x, w1) + b1)

w0 = tf.Variable(tf.zeros([num_units, 10]))
b0 = tf.Variable(tf.zeros([10]))
p = tf.nn.softmax(tf.matmul(hidden1, w0) + b0)


# **[MSL-04]** 오차 함수 loss, 트레이닝 알고리즘 train_step, 정답률 accuracy를 정의한다.

# In[4]:


t = tf.placeholder(tf.float32, [None, 10])
loss = -tf.reduce_sum(t * tf.log(p))
train_step = tf.train.AdamOptimizer().minimize(loss)
correct_prediction = tf.equal(tf.argmax(p, 1), tf.argmax(t, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# **[MSL-05]** 세션을 준비하고 Variable을 초기화한다.

# In[5]:


sess = tf.InteractiveSession()
sess.run(tf.initialize_all_variables())


# **[MSL-06]** 파라미터 최적화를 2000회 반복한다.
#
# 1회 실행할 때마다 트레이닝 세트에서 추출한 100개의 데이터를 이용해 경사 하강법을 적용한다.
#
# 최종적으로 테스트 세트에 대해 약 97%의 정답률을 얻을 수 있다.

# In[6]:


i = 0
for _ in range(2000):
    i += 1
    batch_xs, batch_ts = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, t: batch_ts})
    if i % 100 == 0:
        loss_val, acc_val = sess.run([loss, accuracy],
            feed_dict={x:mnist.test.images, t: mnist.test.labels})
        print ('Step: %d, Loss: %f, Accuracy: %f'
               % (i, loss_val, acc_val))


# **[MSL-07]** 최적홛된 파라미터를 이용해 테스트 세트에 대한 예측을 출력한다.
#
# 여기서는 '0' ~ '9'의 숫자에 대해 정답과 오답 예를 3개씩 출력한다.

# In[7]:


images, labels = mnist.test.images, mnist.test.labels
p_val = sess.run(p, feed_dict={x:images, t: labels})

fig = plt.figure(figsize=(8,15))
for i in range(10):
    c = 1
    for (image, label, pred) in zip(images, labels, p_val):
        prediction, actual = np.argmax(pred), np.argmax(label)
        if prediction != i:
            continue
        if (c < 4 and i == actual) or (c >= 4 and i != actual):
            subplot = fig.add_subplot(10,6,i*6+c)
            subplot.set_xticks([])
            subplot.set_yticks([])
            subplot.set_title('%d / %d' % (prediction, actual))
            subplot.imshow(image.reshape((28,28)), vmin=0, vmax=1,
                           cmap=plt.cm.gray_r, interpolation="nearest")
            c += 1
            if c > 6:
                break

