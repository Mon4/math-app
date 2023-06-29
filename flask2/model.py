import tensorflow as tf
import pickle
from mnist import read_mnist_modified


def model(x_train, y_train, x_test, y_test):
    # normalizacja wartości koloru z 0-255 do 0-1
    x_train = x_train / 255.0,
    x_test = x_test / 255.0

    # budowa warstw sieci neuronowej
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(784, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    # konfiguracja modelu
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # trening modelu
    history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=18, batch_size=256)

    # zapisanie wytrenowanego modelu
    model.save("myModel")

    # zapisanie historii treningu modelu do późniejszego narysowania wykresów
    with open('./trainHistory.pkl', 'wb') as file_pi:
        pickle.dump(history.history, file_pi)


X_train, Y_train, X_test, Y_test = read_mnist_modified()
model(X_train, Y_train, X_test, Y_test)

