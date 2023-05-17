import numpy as np
import cv2
import tensorflow as tf

import image_processing
from image_processing import *


def predict_result(img):
    model = tf.keras.models.load_model('./myModel')
    prediction = model.predict(img.reshape(1, 28, 28)).tolist()[0]
    p = None
    for i in range(10):
        if prediction[i] > 0.5:
            p = i
    return p


def get_digits(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # change representation from RGB to grayscale

    # thresholding - binary mask,
    # values below THRESH_Binary are 0 and higher are 1, OTSU is a method to change threshold
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # binary image

    # finding img's contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sorting contours from left to the right
    sorted_contours = sorted(contours, key=lambda ctr: (cv2.boundingRect(ctr)[0]))

    # create rectangles
    digit_rects = []
    for ctr in sorted_contours:
        x, y, w, h = cv2.boundingRect(ctr)
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 0), 2)  # drawing rectangles
        digit_rects.append((x, y, w, h))

    # drawing contours
    # cv2.imshow('rectangles', gray)
    # cv2.waitKey(0)

    digits = []
    for rect in digit_rects:
        x, y, w, h = rect
        digit = thresh[y:y+h, x:x+w]  # extract
        digits.append(digit)
    return digits 


def prep_digits(digits):
    digits_prep = []
    for d in digits:
        digit_img = Image.fromarray(d)  # cast array to img
        digit_img = image_processing(digit_img)
        digit_a = np.array(digit_img)  # from Image to array (cv)

        # SHOWING IMAGES OF SINGLE DIGITS
        # cv2.imshow('rectangles', digit_a)
        # cv2.waitKey(0)
        #
        # plt.imshow(digit_a, cmap='binary')
        # plt.show()

        digits_prep.append(digit_a)
    return digits_prep


def recognize_numbers(digits_array):
    if len(digits_array) == 0:
        return None
    else:
        number = []
        for digit in digits_array:
            prediction = predict_result(digit)
            number.append(prediction)

        result = []
        for n in number:
            if n is not None:
                result.append(n)

        result = "".join(str(i) for i in result)

        return result


def extract_digits(img):
    digits = get_digits(img)
    digits = prep_digits(digits)
    result = recognize_numbers(digits)

    # print(result)
    return result


# img = cv2.imread('./images/654.png')  # 1 & 2 dimensions are size of image, 3rd is RGB
# print(extract_digits(img))

# img2 = cv2.imread('./images/654.png')
# img4 = cv2.imread('./images/789.png')
# img72 = cv2.imread('./images/987.png')
# extractDigits(img2)
# extractDigits(img4)
# extractDigits(img72)
