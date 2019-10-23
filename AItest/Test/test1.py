import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

version = tf.__version__
gpu_ok = tf.test.is_gpu_available()
print('tensorflow version is ', version)
print('GUP is ', gpu_ok)

