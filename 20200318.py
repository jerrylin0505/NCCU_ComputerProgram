# %matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#1.讀入MNSIT數據集
from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#看數據集內容
# print(len(x_train))
# print(len(x_test))

n = 9487
print(x_train[n])
print(y_train[n])

# plt.imshow(x_train[n], cmap = 'Greys')
# print('正確答案:', y_train[n])

#資料整理
x_train.shape

x_train = x_train.reshape(60000, 784)/255 #顏色總共255號
x_test = x_test.reshape(10000, 784)/255 #顏色總共255號

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
y_train[9487]

#打造神經網路
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense #每一層的神經網路
from tensorflow.keras.optimizers import SGD #學習方式

model = Sequential()

model.add(Dense(87, input_dim = 784, activation = 'relu')) #第一層87個神經元
model.add(Dense(87, activation = 'relu')) #第二層
model.add(Dense(10, activation = 'softmax'))#輸出層 數字全部加起來是1

#組裝Model
model.compile(loss = 'mse', optimizer = SGD(lr = 0.087), metrics = ['accuracy'])
model.summary()

#開始訓練
model.fit(x_train, y_train, batch_size = 100, epochs = 20)

#測試資料預測結果
predict = model.predict_classes(x_test)
n = 9499
print('神經網路預測是:', predict[n])
plt.imshow(x_test[n].reshape(28,28), cmap='Greys')