# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np
import tensorflow as tf
import tensorflow.python.platform
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import warnings

warnings.filterwarnings('ignore')

tf.reset_default_graph()#tensorflowをリセット
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

def cnn(pix,fil,image):
    tf.reset_default_graph()#念のためもう一回リセット
    NUM_CLASSES = 2 #2値分類
    IMAGE_SIZE = pix #画像のサイズ(×縦横)
    IMAGE_4_SIZE = int(IMAGE_SIZE/8)
    IMAGE_PIXELS = IMAGE_SIZE*IMAGE_SIZE*3
    train_txt='./train_c.txt'
    test_txt='./test_c.txt'
    c1_filter = fil

    def inference(images_placeholder, keep_prob):
        # 重みを標準偏差0.1の正規分布で初期化
        def weight_variable(shape):
          initial = tf.truncated_normal(shape, stddev=0.1)
          return tf.Variable(initial)

        # バイアスを標準偏差0.1の正規分布で初期化
        def bias_variable(shape):
          initial = tf.constant(0.1, shape=shape)
          return tf.Variable(initial)

        # 畳み込み層の作成
        def conv2d(x, W):
          return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

        # プーリング層の作成
        def max_pool_2x2(x):
          return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                                strides=[1, 2, 2, 1], padding='SAME')

        # 入力をIMAGE_SIZE^2x3に変形
        x_image = tf.reshape(images_placeholder, [-1, IMAGE_SIZE, IMAGE_SIZE, 3])

        # 畳み込み層1の作成
        with tf.name_scope('conv1') as scope:
            W_conv1 = weight_variable([5, 5, 3, c1_filter])
            b_conv1 = bias_variable([c1_filter])
            h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

        # プーリング層1の作成
        with tf.name_scope('pool1') as scope:
            h_pool1 = max_pool_2x2(h_conv1)

        # 畳み込み層2の作成
        with tf.name_scope('conv2') as scope:
            W_conv2 = weight_variable([5, 5, c1_filter, c1_filter*2])
            b_conv2 = bias_variable([c1_filter*2])
            h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)

        # プーリング層2の作成
        with tf.name_scope('pool2') as scope:
            h_pool2 = max_pool_2x2(h_conv2)

        # 畳み込み層3の作成
        with tf.name_scope('conv3') as scope:
            W_conv3 = weight_variable([5, 5, c1_filter*2, c1_filter*4])
            b_conv3 = bias_variable([c1_filter*4])
            h_conv3 = tf.nn.relu(conv2d(h_pool2, W_conv3) + b_conv3)

        # プーリング層3の作成
        with tf.name_scope('pool3') as scope:
            h_pool3 = max_pool_2x2(h_conv3)

        # 全結合層1の作成
        with tf.name_scope('fc1') as scope:
            W_fc1 = weight_variable([IMAGE_4_SIZE*IMAGE_4_SIZE*c1_filter*4, 512])
            b_fc1 = bias_variable([512])
            h_pool3_flat = tf.reshape(h_pool3, [-1, IMAGE_4_SIZE*IMAGE_4_SIZE*c1_filter*4])
            h_fc1 = tf.nn.relu(tf.matmul(h_pool3_flat, W_fc1) + b_fc1)
            # dropoutの設定
            h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

        # 全結合層2の作成
        with tf.name_scope('fc2') as scope:
            W_fc2 = weight_variable([512, NUM_CLASSES])
            b_fc2 = bias_variable([NUM_CLASSES])

        # ソフトマックス関数による正規化
        with tf.name_scope('softmax') as scope:
            y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

        # 各ラベルの確率のようなものを返す
        return y_conv



    def accuracy(logits, labels):
        correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        tf.summary.scalar("accuracy", accuracy)
        return accuracy

    def predict(input):

        predict=tf.argmax(input,1)
        return predict

    # f = open(test_txt, 'r')
    # test_image = []
    # test_label = []
    # for line in f:
    #     line = line.rstrip()
    #     l = line.split()
    #     if(len(l)==2):
    #         img = cv2.imread(l[0])
    #         img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
    #         test_image.append(img.flatten().astype(np.float32)/255.0)
    #         tmp = np.zeros(NUM_CLASSES)
    #         tmp[int(l[1])] = 1
    #         test_label.append(tmp)
    # test_image = np.asarray(test_image)
    # test_label = np.asarray(test_label)
    # f.close()

    input_image = []
    img = image
    img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
    input_image.append(img.flatten().astype(np.float32)/255.0)
    input_image = np.asarray(input_image)

    with tf.Graph().as_default():
        # 画像を入れる仮のTensor
        images_placeholder = tf.placeholder("float", shape=(None, IMAGE_PIXELS))
        # ラベルを入れる仮のTensor
        labels_placeholder = tf.placeholder("float", shape=(None, NUM_CLASSES))
        # dropout率を入れる仮のTensor
        keep_prob = tf.placeholder("float")

        # inference()を呼び出してモデルを作る
        logits = inference(images_placeholder, keep_prob)
        # 精度の計算
        acc = accuracy(logits, labels_placeholder)

        pred = predict(logits)

        # 保存の準備
        saver = tf.train.Saver()
        # Sessionの作成
        sess = tf.Session()
        # 変数の初期化
        sess.run(tf.initialize_all_variables())
        # モデルを復元
        saver.restore(sess, "./modelcp3/model.ckpt")


    test_pred=sess.run(pred, feed_dict={
        images_placeholder: input_image,
        keep_prob: 1.0})


    return(int(test_pred))
