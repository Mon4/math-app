from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
import collections
from scipy.stats import chisquare
from mnist import read_mnist


def histogram(y_test, y_train):
    # transforming data, connecting and selecting number of digits
    y = np.append(y_test, y_train)
    data = list(collections.OrderedDict(sorted(dict(Counter(y)).items())).values())
    print(data)
    expected = [6960.8] * 10
    chi2, p_value = chisquare(data)
    # p_value = float(p_value)

    print(chi2, p_value)

    # plotting
    plt.bar(np.arange(10), data)
    plt.xticks(np.arange(10))
    plt.xlabel("cyfra")
    plt.ylabel("liczba obrazków")
    plt.show()


def sample_mnist():
    images_dict = {}
    for i in range(len(x_train)):
        label = y_train[i]
        if label not in images_dict:
            images_dict[label] = []
        images_dict[label].append(x_train[i])

    # wyświetlenie posortowanych obrazów
    fig, axs = plt.subplots(10, 10, figsize=(8, 8))
    for i in range(10):
        for j in range(10):
            axs[i, j].imshow(np.zeros((28, 28)), cmap='binary')
            if i * 10 + j < len(images_dict[i]):
                axs[i, j].imshow(images_dict[i][j], cmap='binary')
                axs[i, j].axis('off')
    plt.show()


def before_augmentatio(X_train, Y_train):
    num_row = 2
    num_col = 8
    num = num_row*num_col
    fig1, axes1 = plt.subplots(num_row, num_col, figsize=(1.5 * num_col, 2 * num_row))
    for i in range(num):
        ax = axes1[i // num_col, i % num_col]
        ax.imshow(X_train[i], cmap='gray_r')
        ax.set_title('Label: {}'.format(Y_train[i]))
    plt.tight_layout()
    plt.show()


x_train, y_train, x_test, y_test = read_mnist()
before_augmentatio(x_train, y_train)
histogram(y_test, y_train)
sample_mnist()



