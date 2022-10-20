# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import tensorflow as tf
import tensorflow_datasets as tfds


def resize(image, label):
    """图像预处理"""
    image = tf.image.resize(image, [224, 224]) / 255.0
    return image, label


strategy = tf.distribute.MirroredStrategy()
batch_size = 64 * strategy.num_replicas_in_sync  # 批次大小×设备数量

dataset = tfds.load('cats_vs_dogs', split=tfds.Split.TRAIN, as_supervised=True)
dataset = dataset.map(resize).shuffle(1024).batch(batch_size)

with strategy.scope():
    model = tf.keras.applications.MobileNetV2(weights=None, classes=2)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss=tf.keras.losses.sparse_categorical_crossentropy,
        metrics=[tf.keras.metrics.sparse_categorical_accuracy]
    )

print('Number of devices: {}'.format(strategy.num_replicas_in_sync))
model.fit(dataset, epochs=5)
# Number of devices: 4
# Epoch 1/5
# 91/91 [==============================] - 35s 390ms/step - loss: 0.6459 - sparse_categorical_accuracy: 0.6374
# Epoch 2/5
# 91/91 [==============================] - 34s 377ms/step - loss: 0.5499 - sparse_categorical_accuracy: 0.7225
# Epoch 3/5
# 91/91 [==============================] - 34s 373ms/step - loss: 0.4560 - sparse_categorical_accuracy: 0.7826
# Epoch 4/5
# 91/91 [==============================] - 35s 382ms/step - loss: 0.3811 - sparse_categorical_accuracy: 0.8285
# Epoch 5/5
# 91/91 [==============================] - 34s 379ms/step - loss: 0.3274 - sparse_categorical_accuracy: 0.8558
