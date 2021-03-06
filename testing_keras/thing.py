from keras.layers.core import Dense, Activation
from keras.models import Sequential
from keras.datasets import mnist

model = Sequential()

model.add(Dense(output_dim=64, input_dim=100, init="glorot_uniform"))
model.add(Activation("relu"))
model.add(Dense(output_dim=10, init="glorot_uniform"))
model.add(Activation("softmax"))

model.compile(loss='categorical_crossentropy', optimizer='sgd')

(X_train,y_train),(X_test,y_test) = mnist.load_data()

print len(X_train)

model.fit(X_train,y_train,nb_epoch=5,batch_size=32)
#objective_score = model.evaluate(X_test, y_test, batch_size=32)
#print objective_score
