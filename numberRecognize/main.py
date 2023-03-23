import numpy as np
import tensorflow as tf
from keras.datasets import mnist
from matplotlib import pyplot as plt
from tensorflow.python.ops.confusion_matrix import confusion_matrix
import seaborn as sn


(x_train, y_train), (x_test, y_test) = mnist.load_data()
# normalization color values from 0-255 to 0-1
x_train = x_train / 255.0,
x_test = x_test / 255.0

# Flattening is converting the data into a 1-dimensional array
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(784, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=20, batch_size=200)

model.save("myModel")


# statistics
scores = model.evaluate(x_test, y_test, verbose=0)
predicted = model.predict(x_test)
predicted = np.argmax(predicted, axis=1)

cm = confusion_matrix(y_test, predicted)
sn.heatmap(cm, cmap='Blues', annot=True, fmt='g')
plt.title(label="Macierz błędu")
plt.show()

# FP = confusion_matrix.sum(axis=0) - np.diag(confusion_matrix)
# FN = confusion_matrix.sum(axis=1) - np.diag(confusion_matrix)
# TP = np.diag(confusion_matrix)
# TN = confusion_matrix.values.sum() - (FP + FN + TP)
#
# # Sensitivity, hit rate, recall, or true positive rate
# TPR = TP/(TP+FN)
# # Specificity or true negative rate
# TNR = TN/(TN+FP)
# # Precision or positive predictive value
# PPV = TP/(TP+FP)
# # Negative predictive value
# NPV = TN/(TN+FN)
# # Fall out or false positive rate
# FPR = FP/(FP+TN)
# # False negative rate
# FNR = FN/(TP+FN)
# # False discovery rate
# FDR = FP/(TP+FP)
#
# # Overall accuracy
# ACC = (TP+TN)/(TP+FP+FN+TN)

print("Baseline Error: %.2f%%" % (100-scores[1]*100))


def classify(input):
    prediction = model.predict(input.reshape(1, 28, 28)).tolist()[0]
    return {str(i): prediction[i] for i in range(10)}


# # gradio website
# label = gr.outputs.Label(num_top_classes=3)
# interface = gr.Interface(fn=classify, inputs="sketchpad", outputs=label, live=True)
# interface.launch()

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('accuracy function')
plt.ylabel('dokładność')
plt.xlabel('epoki')
plt.legend(['train', 'test'], loc='upper left')
# summarize history for loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('funkcja strat')
plt.ylabel('straty')
plt.xlabel('epoki')
plt.legend(['train', 'test'], loc='upper right')
plt.show()


