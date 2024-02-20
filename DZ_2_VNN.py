import keras
from keras.layers import *
import matplotlib.pyplot as plt
import numpy as np
import keras.utils
from PIL import Image

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# plt.imshow(x_train[0])
# for i in range(16):
#   plt.subplot(4,4,i+1)
#   plt.imshow(x_train[i])
# plt.show()

input_shape = (28, 28, 1)

x_train = x_train / 255
x_test = x_test / 255

y_train_cat = keras.utils.to_categorical(y_train, 10)
y_test_cat = keras.utils.to_categorical(y_test, 10)

model_2 = keras.Sequential([
keras.Input(shape=input_shape),
Flatten(),
Dense(50, activation = 'relu'),
Dense(10, activation = 'softmax')
] )

model_2.compile(optimizer='adam',
loss='categorical_crossentropy',
metrics=['accuracy'])

%%time

model_2.fit(x_train, y_train_cat, batch_size=32, epochs=5)

with Image.open("img8.jpg") as im:
   img = Image.load_img(im, target_size=(28, 28))
img_tensor = Image.img_to_array(img)
img_tensor = np.expand_dims(img_tensor, axis=0)
img_tensor /= 255.
prediction = model_2.predict(img_tensor)
print (prediction)