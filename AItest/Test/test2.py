# 测试tensorflow中的keras库

from tensorflow import keras

(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()
# print(train_images.shape)
# print(test_images.shape)
# print(len(train_labels))
# print(len(test_labels))
# print(train_labels)
# print(test_labels)

# tensorflow中的头文件调用
# tensorflow_head_file = ('tensorflow.python',
#                         'tensorflow.tools',
#                         'tensorflow.core',
#                         'tensorflow.compiler',
#                         'tensorflow.lite',
#                         'tensorflow.keras',
#                         'tensorflow.compat',
#                         'tensorflow.summary',
#                         'tensorflow.examples')
