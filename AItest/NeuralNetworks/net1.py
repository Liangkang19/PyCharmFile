# 使用Tensorflow中的keras，初步搭建训练模型

from __future__ import absolute_import, division, print_function, unicode_literals

from tensorflow import keras

mnist = keras.datasets.mnist                               # 新的引用格式
(x_train, y_train), (x_test, y_test) = mnist.load_data()   # 载入MNIST数据集
x_train, x_test = x_train / 255.0, x_test / 255.0          # 将样本从整数转换为浮点数

# 将模型的各层堆叠起来，以搭建 keras.Sequential 模型。为训练选择优化器和损失函数。
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 训练并验证模型
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test,  y_test, verbose=2)
