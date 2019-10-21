import tensorflow as tf
import numpy as np
import time
from IPython import display
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing


class LSTM(tf.keras.Model):
    def __init__(self, timesteps, hiddenunits):
        self.timesteps = timesteps
        self.hidden = hiddenunits
        super(LSTM, self).__init__()
        self.lstm = tf.keras.Sequential(
            [
                tf.keras.layers.InputLayer(input_shape=(self.timesteps, 1)),
                tf.keras.layers.LSTM(self.hidden, return_sequences=False, use_bias=True),
                tf.keras.layers.Dense(1,activation='linear',use_bias=True)
            ]
        )

    @tf.function
    def sample(self, input):
        return self.lstm(input)


@tf.function
def compute_loss(model, x, y, loss='MSE'):  # 定义三种损失函数
    pred = model.sample(x)
    if loss == 'MAE':
        return tf.losses.mean_absolute_error(y, pred)
    if loss == 'MSE':
        return tf.losses.mean_squared_error(y, pred)
    if loss == 'MAPE':
        return tf.losses.mean_absolute_percentage_error(y, pred)


@tf.function
def compute_apply_gradients(model, x, y, optimizer):
    with tf.GradientTape() as tape:
        loss = compute_loss(model, x, y)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))


def train_lstm(epochs, train_dataset, test_dataset, model, optimizer,scaler,timesteps,data):
    train_pred = []
    test_pred = []
    train_real = []
    test_real = []

    def inverse(x):
        x = np.array(x).reshape(-1, 1)
        x = scaler.inverse_transform(x).reshape(1, -1)[0]
        return x
    for train_x, train_y in train_dataset:
        train_real += train_y.numpy().flatten().tolist()
    for test_x, test_y in test_dataset:
        test_real += test_y.numpy().flatten().tolist()
    print(train_real)
    train_real = inverse(train_real)
    print('-'*40)
    print(train_real)
    test_real = inverse(test_real)
    train_mape = []
    test_mape = []

    def predict_futrue(n=10):
        res = []
        last = data[-timesteps:]
        for i in range(n):
            pred = model.sample(last.reshape((1,)+last.shape))
            temp = pred.numpy().flatten().tolist()
            res += temp
            print(temp)
            last = np.array(last.reshape(1, -1)[0].tolist()[1:]+temp).reshape(-1, 1).astype(np.float32)
            print(last)
            print(last.shape, '-'*20)
        return inverse(res)
    for epoch in range(1, epochs + 1):
        train_pred = []
        test_pred = []
        start_time = time.time()
        for train_x, train_y in train_dataset.shuffle(buffer_size=300):
            compute_apply_gradients(model, train_x, train_y, optimizer)

        end_time = time.time()

        if epoch % 20 == 0:
            loss = tf.keras.metrics.Mean()
            loss_train = tf.keras.metrics.Mean()
            for test_x, test_y in test_dataset:
                loss(compute_loss(model, test_x, test_y, loss='MAPE'))
            for train_x, train_y in train_dataset:
                loss_train(compute_loss(model, train_x, train_y, loss='MAPE'))
            elbo = loss.result()
            test_mape.append(elbo)
            train_mape.append(loss_train.result())
            display.clear_output(wait=False)
            print('Epoch: {}, Test set ELBO: {}, '
                  'time elapse for current epoch {}'.format(epoch,
                                                            elbo,
                                                            end_time - start_time))

        if epoch % 100 == 0:
            prediction = predict_futrue(10)
            train_pred = []
            test_pred = []
            for train_x, train_y in train_dataset:
                train_pred += model.sample(train_x).numpy().flatten().tolist()
            for test_x, test_y in test_dataset:
                test_pred += model.sample(test_x).numpy().flatten().tolist()
            train_pred = inverse(train_pred)

            test_pred = inverse(test_pred)
            plt.figure()
            plt.plot(range(1 + timesteps, timesteps + len(train_pred) + 1), np.array(train_pred), color='r',
                     label='train_pred')
            plt.plot(range(1 + timesteps, timesteps + len(train_pred) + 1), np.array(train_real), color='y',
                     label='train_real')
            plt.plot(range(timesteps + len(train_pred) + 1, timesteps + len(train_pred) + 1 + len(test_pred)),
                     np.array(test_pred),
                     color='b', label='test_pred')
            plt.plot(range(timesteps + len(train_pred) + 1, timesteps + len(train_pred) + 1 + len(test_real)),
                     np.array(test_real),
                     color='c', label='test_real')
            plt.plot(range(timesteps + len(train_pred) + 1 + len(test_real),
                           timesteps + len(train_pred) + 1 + len(test_real) + len(prediction)), np.array(prediction),
                     color='g', label='prediction')
            plt.legend()
            plt.title('epoch '+str(epoch)+'   timesteps='+str(timesteps))
            plt.xlabel('month')
            plt.show()

    plt.figure()
    # plt.subplot(211)
    plt.plot(20 * np.array(range(len(train_mape))), train_mape, color='r', label='training mape')
    plt.plot(20 * np.array(range(len(test_mape))), test_mape, color='b', label='testing mape')
    plt.legend()
    plt.title('mape'+'   timesteps='+str(timesteps))
    plt.xlabel('epochs')
    plt.show()


def get_dataset(x, num_test=6, timesteps=4):
    num_train = x.shape[0] - num_test
    x_train = np.empty([num_train - timesteps, timesteps, x.shape[1]], dtype=np.float32)
    y_train = np.empty(num_train - timesteps, dtype=np.float32)
    x_test = np.empty([num_test, timesteps, x.shape[1]], dtype=np.float32)
    y_test = np.empty(num_test, dtype=np.float32)
    for i in range(x_train.shape[0]):
        x_train[i] = x[i:i + timesteps]
        y_train[i] = x[i + timesteps]
    for j in range(x_test.shape[0]):
        x_test[j] = x[j + num_train - timesteps:j + num_train]
        y_test[j] = x[j + num_train]
    return x_train, y_train, x_test, y_test


if __name__ == '__main__':
    shuju = 1
    if shuju == 1:  # 42点数据
        data = pd.read_csv('file.csv').values
        min_max_scaler = preprocessing.StandardScaler()  # 做归一化
        # min_max_scaler = preprocessing.MinMaxScaler((0.1,0.9))
        data = min_max_scaler.fit_transform(data).astype(np.float32)
        timesteps = 7    # 时间步长
        x_train, y_train, x_test, y_test = get_dataset(data, num_test=6, timesteps=timesteps) # 生成训练和测试集合
        print(x_train.dtype)

        TRAIN_BUF = 300
        BATCH_SIZE = 2
        TEST_BUF = 100
        train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(BATCH_SIZE)#tensorflow数据集迭代器
        test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(BATCH_SIZE)

        optimizer = tf.keras.optimizers.Adam(1e-4)  # 损失函数
        model = LSTM(timesteps=timesteps, hiddenunits=10)  # 所用lstm模型
        train_lstm(epochs=5000, train_dataset=train_dataset, test_dataset=test_dataset, model=model, optimizer=optimizer, scaler=min_max_scaler, timesteps=timesteps, data=data)
    if shuju == 2:  # 256点数据
        df = pd.read_csv('data2.csv')
        value = df.columns.values.tolist()
        data = [float(x) for x in value]
        data = np.array(data).reshape(-1, 1).astype(np.float32)
        min_max_scaler2 = preprocessing.MinMaxScaler((0.1, 0.9))
        data = min_max_scaler2.fit_transform(data)
        timesteps = 8
        x_train, y_train, x_test, y_test = get_dataset(data, num_test=48, timesteps=timesteps)
        print(x_train.dtype)

        TRAIN_BUF = 300
        BATCH_SIZE = 2
        TEST_BUF = 100
        train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(BATCH_SIZE)
        test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(BATCH_SIZE)

        optimizer = tf.keras.optimizers.Adam(1e-4)
        model = LSTM(timesteps=timesteps, hiddenunits=100)
        train_lstm(epochs=5000, train_dataset=train_dataset, test_dataset=test_dataset, model=model,
                   optimizer=optimizer, scaler=min_max_scaler2, timesteps=timesteps, data=data)

