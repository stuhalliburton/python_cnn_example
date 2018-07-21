import keras
from keras.models import load_model
import os

save_dir = os.path.join(os.getcwd(), 'saved_models')
model_name = 'keras_cifar10_trained_model.h5'
model_path = os.path.join(save_dir, model_name)

model = load_model(model_path)

from keras.datasets import cifar10
num_classes = 10
# The data, split between train and test sets:
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print('x_train shape:', x_train.shape)

# Convert class vectors to binary class matrices.
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print y_train[1]

# import matplotlib.pyplot as plt
# plt.imshow(x_train[1])
# plt.show()

import np
img = np.array(x_train[1])
img = img.reshape((1, 32, 32, 3))
print model.predict(img)
