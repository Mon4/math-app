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


x_train, y_train, x_test, y_test = read_mnist()
histogram(y_test, y_train)
sample_mnist()


