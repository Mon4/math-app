import numpy as np
from keras_preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from mnist import *
from sklearn.model_selection import train_test_split


def plot_before(num_row, num_col, num, X_train, Y_train):
    fig1, axes1 = plt.subplots(num_row, num_col, figsize=(1.5 * num_col, 2 * num_row))
    for i in range(num):
        ax = axes1[i // num_col, i % num_col]
        ax.imshow(X_train[i], cmap='gray_r')
        ax.set_title('Label: {}'.format(Y_train[i]))
    plt.tight_layout()
    plt.show()


def augment(num_row, num_col, num, X_train, Y_train, datagen):
    X_augmented = np.empty((0, 28, 28))
    Y_augmented = np.empty((0,))
    fig2, axes2 = plt.subplots(num_row, num_col, figsize=(1.5 * num_col, 2 * num_row))

    for X, Y in datagen.flow(X_train.reshape(X_train.shape[0], 28, 28, 1), Y_train.reshape(Y_train.shape[0], 1),
                             batch_size=num, shuffle=False):
        for j in range(0, 8):
            # ax = axes2[j // num_col, j % num_col] # 2D
            ax = axes2[j % num_col]
            ax.imshow(X[j].reshape(28, 28), cmap='gray_r')
            ax.set_title('Label: {}'.format(int(Y[j])))

        for i in range(0, num):
            if i % 1000 == 0:
                print(i, ", %.1f%%" % (i/num*100))
            X_augmented = np.append(X_augmented, [X[i].reshape(28, 28)], axis=0)
            Y_augmented = np.append(Y_augmented, int(Y[i]))

        break
    plt.tight_layout()
    plt.show()
    return X_augmented, Y_augmented


def split_data(X_train, Y_train, X_test, Y_test, split_ratio):
    x = np.concatenate([X_train, X_test], axis=0)
    y = np.append(Y_train, Y_test)
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=split_ratio, random_state=25)
    return X_train, Y_train, X_test, Y_test


def main_augmentation():
    X_train, Y_train, X_test, Y_test = read_mnist()
    X_train, Y_train, X_test, Y_test = split_data(X_train, Y_train, X_test, Y_test, 0.5)
    # CONSTS
    num_col = 8
    num_row = 1
    num = 20000  # number of new data
    rotation_range_val = 30  # max angle value
    width_shift_val = 0.25
    height_shift_val = 0.25
    shear_range_val = 45
    zoom_range_val = [0.5, 1.5]

    # plot_before(num_row, num_col, num, X_train, Y_train)

    datagen = ImageDataGenerator(rotation_range=rotation_range_val,
                                 width_shift_range=width_shift_val,
                                 height_shift_range=height_shift_val,
                                 shear_range=shear_range_val,
                                 zoom_range=zoom_range_val)

    datagen.fit(X_train.reshape(X_train.shape[0], 28, 28, 1))

    # add augmented images to dataset
    X_augmented, Y_augmented = augment(num_row, num_col, num, X_train, Y_train, datagen)
    X_train = np.concatenate([X_train, X_augmented], axis=0)
    Y_train = np.append(Y_train, Y_augmented)

    # X_train, Y_train, X_test, Y_test = split_data(X_train, Y_train, X_test, Y_test, 0.3)

    save_mnist_modified(X_train, Y_train, X_test, Y_test)
    print("whatever")


main_augmentation()
