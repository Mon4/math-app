import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
from matplotlib import pyplot as plt

import image_processing
from image_processing import *

def predict_result(img):
    prediction = model.predict(img.reshape(1, 28, 28)).tolist()[0]
    # value_when_true if condition else value_when_false
    p = None
    for i in range(10):
        if prediction[i] > 0.5:
            p = i
    return p


def sort_contours(contours):
    for ctr in contours:
        x, y, w, h = cv2.boundingRect(ctr)
    return 0

def get_digits(img):
    # gray = to_grayscale(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # treshholding - binary mask to find where are pixels
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # finding img's contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sorting contours to be signed from left to the right - by center of image
    sorted_contours = sorted(contours, key=lambda ctr: (cv2.boundingRect(ctr)[0]))


    # create rectangles
    digit_rects = []
    for ctr in sorted_contours:
        x, y, w, h = cv2.boundingRect(ctr)
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 0), 2)  # drawing rectangles
        digit_rects.append((x, y, w, h))

    # drawing contours
    # cv2.imshow('image', gray_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # for every rect extract digit
    digits = []
    for rect in digit_rects:
        x, y, w, h = rect
        digit = thresh[y:y+h, x:x+w]  # extract

        plt.imshow(digit, interpolation='nearest', cmap='gray')
        plt.show()

        digit_img = Image.fromarray(digit)  # cast array to img
        digit_img = image_processing(digit_img)
        digit_a = np.array(digit_img) # from Image to array (cv)

        plt.imshow(digit_a, interpolation='nearest', cmap='gray')
        plt.show()

        digits.append(digit_a)


    digits_array = []
    for digit in digits:
        digit = np.array(digit)
        digit = digit.astype('float32') / 255.0
        digit = digit.reshape(1, 28, 28, 1)
        digits_array.append(digit)

    return digits_array


def recognize_numbers(digits_array):
    number = []
    for digit in digits_array:
        prediction = predict_result(digit)
        number.append(prediction)

    result = []
    for n in number:
        if n is not None:
            result.append(n)
        # else:
        #     result.append(n)
        #     break

    result = "".join(str(i) for i in result)


    print(result)
    return result


# read img
img2 = cv2.imread('123.png')
img = Image.open('1234567890.png')

digit_array = get_digits(img2)
model = tf.keras.models.load_model('./myModel')
result = recognize_numbers(digit_array)



#img_array = np.array(img) # from Image to array (cv)
#img = Image.fromarray(img_array) # from array