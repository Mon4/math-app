import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
from matplotlib import pyplot as plt


def predict_result(img):
    prediction = model.predict(img.reshape(1, 28, 28)).tolist()[0]
    # value_when_true if condition else value_when_false
    p = None
    for i in range(10):
        if prediction[i] > 0.5:
            p = i
    return p

def get_digits(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray, interpolation='nearest')
    #plt.show()

    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


    # finding img's contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # create rectangles
    digit_rects = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        digit_rects.append((x, y, w, h))

    # for every rect extract digit
    digits = []
    for rect in digit_rects:
        x, y, w, h = rect
        digit = gray[y:y+h, x:x+w]
        digit = cv2.resize(digit, (28, 28), interpolation=cv2.INTER_AREA)
        digits.append(digit)

        plt.imshow(digit, interpolation='none')
        plt.show()

    digits_array = []
    for digit in digits:
        digit = np.array(digit)
        digit = digit.astype('float32') / 255.0
        digit = digit.reshape(1, 28, 28, 1)
        digits_array.append(digit)

    result = []
    for digit in digits_array:
        prediction = predict_result(digit)
        result.append(prediction)

    r = "".join(str(i) for i in result)
    print(r)
    return r


# read img
img = cv2.imread('72.png')
# plt.imshow(img, interpolation='nearest')
# #plt.show()
model = tf.keras.models.load_model('./myModel')
get_digits(img)