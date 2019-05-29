from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from keras import metrics

model = Sequential() #linear stack of layers

model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu', input_shape=(20,216,1)))
model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,3), strides=(2,3)))

model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,3), strides=(2,3)))

model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,3), strides=(2,3)))

model.add(Flatten())
model.add(Dense(5, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])