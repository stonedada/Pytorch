# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import tensorflow as tf
import tensorflow_datasets as tfds


def resize(image, label):
    """图像预处理"""
    image = tf.image.resize(image, [224, 224]) / 255.0
    return image, label


batch_size = 64
dataset = tfds.load('cats_vs_dogs', split=tfds.Split.TRAIN, as_supervised=True)
dataset = dataset.map(resize).shuffle(1024).batch(batch_size)

model = tf.keras.applications.MobileNetV2(weights=None, classes=2)
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.sparse_categorical_crossentropy,
    metrics=[tf.keras.metrics.sparse_categorical_accuracy]
)

model.fit(dataset, epochs=5)
# Epoch 1/5
# 364/364 [==============================] - 110s 303ms/step - loss: 0.6229 - sparse_categorical_accuracy: 0.6500
# Epoch 2/5
# 364/364 [==============================] - 111s 305ms/step - loss: 0.4781 - sparse_categorical_accuracy: 0.7690
# Epoch 3/5
# 364/364 [==============================] - 110s 301ms/step - loss: 0.3919 - sparse_categorical_accuracy: 0.8202
# Epoch 4/5
# 364/364 [==============================] - 113s 311ms/step - loss: 0.3171 - sparse_categorical_accuracy: 0.8602
# Epoch 5/5
# 364/364 [==============================] - 113s 311ms/step - loss: 0.2532 - sparse_categorical_accuracy: 0.8919
