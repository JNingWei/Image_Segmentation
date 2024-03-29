# coding=utf-8

"""
Image-Segmentation
Test fcn32_vgg.
__author__ = 'JNingWei'
"""

import os
import scipy as scp
import scipy.misc

import numpy as np
import tensorflow as tf

import fcn32_vgg
import utils

from tensorflow.python.framework import ops

img1 = scp.misc.imread(os.getcwd()[:-3] + 'test_data/pretty_girl.jpg')


with tf.Session() as sess:
    images = tf.placeholder("float")
    feed_dict = {images: img1}
    batch_images = tf.expand_dims(images, 0)

    vgg_fcn = fcn32_vgg.FCN32VGG()
    with tf.name_scope("content_vgg"):
        vgg_fcn.build(batch_images, debug=True)

    print('Finished building Network.')

    init = tf.global_variables_initializer()
    sess.run(init)

    print('Running the Network')
    tensors = [vgg_fcn.pred, vgg_fcn.pred_up]
    down, up = sess.run(tensors, feed_dict=feed_dict)

    down_color = utils.color_image(down[0])
    up_color = utils.color_image(up[0])

    scp.misc.imsave(os.getcwd()[:-3] + 'generated_image/fcn32_downsampled.jpg', down_color)
    scp.misc.imsave(os.getcwd()[:-3] + 'generated_image/fcn32_upsampled.jpg', up_color)
