import pickle
from keras.datasets import mnist


def read_mnist():
    with open('mnist.pkl', 'rb') as f:
        X_train, Y_train, X_test, Y_test = pickle.load(f, encoding='latin1')
    return X_train, Y_train, X_test, Y_test


def save_mnist():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    mnist_data = x_train, y_train, x_test, y_test
    with open('mnist.pkl', 'wb') as f:
        pickle.dump(mnist_data, f)


def read_mnist_modified():
    with open('mnist_modified.pkl', 'rb') as f:
        X_train, Y_train, X_test, Y_test = pickle.load(f, encoding='latin1')
    return X_train, Y_train, X_test, Y_test


def save_mnist_modified(X_train, Y_train, X_test, Y_test):
    mnist_data = X_train, Y_train, X_test, Y_test
    with open('mnist_modified.pkl', 'wb') as f:
        pickle.dump(mnist_data, f)
