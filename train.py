import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.callbacks import EarlyStopping

from model import model
from preprocessing import genre_list

X = np.load('extracted.npy')[:,:,:,None]
y = np.load('labels.npy')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=np.argmax(y, 1), random_state=2615)

es = EarlyStopping(monitor='val_loss', mode='min', patience=5)
model.fit(X_train, y_train, batch_size=8, epochs=1000, validation_split=0.25, callbacks=[es])

print(model.evaluate(X_test, y_test))

model.save('my_model.linh')
from keras.models import load_model
del model
model = load_model('my_model.linh')
print(model.evaluate(X_test, y_test))