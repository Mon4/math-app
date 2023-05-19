from sklearn.metrics import confusion_matrix
from mnist import read_mnist_modified
import numpy as np
import pickle
import tensorflow as tf
import seaborn as sn
import matplotlib.pyplot as plt


def plots():
    plt.subplot(1, 2, 1)
    plt.plot(history['accuracy'])
    plt.plot(history['val_accuracy'])
    plt.title('funkcja dokładności')
    plt.ylabel('dokładność')
    plt.xlabel('epoki')
    plt.legend(['train', 'test'], loc='upper left')
    # summarize history for loss
    plt.subplot(1, 2, 2)
    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    plt.title('funkcja strat')
    plt.ylabel('straty')
    plt.xlabel('epoki')
    plt.legend(['train', 'test'], loc='upper right')
    plt.tight_layout()
    plt.show()


def confision():
    cm = confusion_matrix(y_test, predicted)
    sn.heatmap(cm, cmap='Blues', annot=True, fmt='g')
    plt.title(label="Macierz błędu")
    plt.xlabel("wartości przewidywane")
    plt.ylabel("wartości prawdziwe")
    plt.tight_layout()
    plt.show()
    return cm


def stats():
    scores = model.evaluate(x_test, y_test, verbose=0)
    predicted = model.predict(x_test)
    predicted = np.argmax(predicted, axis=1)

    print("accuracy: %.2f%%" % (scores[1]*100))
    return predicted


def precision():
    FP = cm.sum(axis=0) - np.diag(cm)
    FN = cm.sum(axis=1) - np.diag(cm)
    TP = np.diag(cm)
    TN = cm.sum() - (FP + FN + TP)
    # Sensitivity, hit rate, recall, or true positive rate
    TPR = TP/(TP+FN)
    # Specificity or true negative rate
    TNR = TN/(TN+FP)
    # Precision or positive predictive value
    PPV = TP/(TP+FP)
    print("TP", TP)
    print("TN", TN)
    print("FP", FP)
    print("FN", FN)

    print("recall: ", TPR.round(2))
    print("specificity: ", TNR.round(2))
    print("precision: ", PPV.round(2))


# reading data
with open('./trainHistory.pkl', 'rb') as file:
    history = pickle.load(file)

x_train, y_train, x_test, y_test = read_mnist_modified()

model = tf.keras.models.load_model('./myModel')
# statistics

predicted = stats()
# plots()
cm = confision()
precision()


# # Negative predictive value
# NPV = TN/(TN+FN)
# # Fall out or false positive rate
# FPR = FP/(FP+TN)
# # False negative rate
# FNR = FN/(TP+FN)
# # False discovery rate
# FDR = FP/(TP+FP)


# # gradio website
# label = gr.outputs.Label(num_top_classes=3)
# interface = gr.Interface(fn=classify, inputs="sketchpad", outputs=label, live=True)
# interface.launch()


