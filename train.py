
import numpy as np
from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import keras
import cv2

WIDTH = 300
HEIGHT = 100
CHANNELS=1
EPOCHS = 30
num_classes=1
test_samples=5000
prev_mean=10
prev_std=10

model = Sequential()
model.add(Conv2D(24, kernel_size=(5, 5), strides=(2, 2),activation='tanh',input_shape=(WIDTH,HEIGHT,CHANNELS)))
model.add(Conv2D(36, kernel_size=(5, 5), strides=(2, 2),activation='tanh'))
model.add(Conv2D(48, kernel_size=(5, 5), strides=(2, 2),activation='tanh'))
model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1),activation='tanh'))
model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1),activation='tanh'))
model.add(Flatten())
model.add(Dense(1000, activation='tanh'))
model.add(Dense(100, activation='tanh'))
model.add(Dense(50,activation='tanh'))
model.add(Dense(1, activation='linear'))
model.compile(loss="mean_squared_error", optimizer='adam', metrics=['accuracy'])

class TestCallback(keras.callbacks.Callback):
    def __init__(self, test_data):
        self.test_data = test_data

    def on_epoch_end(self, epoch, logs={}):
        predictions= self.model.predict(test_x)
        diff=predictions.flatten()-test_y
        mean = np.mean(diff)
        std = np.std(diff)
        print('mean:',mean,'std: ',std)

train_data = np.load("dataset_no_zeros.npy")
print(len(train_data))
train = train_data[:-test_samples]
test = train_data[-test_samples:]
X=[i[0] for i in train]
Y = [i[1] for i in train]
test_x = np.array([i[0] for i in test])
test_y = [i[1] for i in test]
X=np.array(X).reshape(-1,WIDTH,HEIGHT,CHANNELS)
test_x=np.array(test_x).reshape(-1,WIDTH,HEIGHT,CHANNELS)
model.fit(X, Y, validation_data=(test_x, test_y),callbacks=[TestCallback((test_x, test_y))],epochs=EPOCHS,shuffle=True)
model.save('models')
