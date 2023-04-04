import os
import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, request
from image_processing import *

model = tf.keras.models.load_model('./myModel')


def prepare_image(img):
    img = np.array(img)
    return img

def predict_result(img):
    prediction = model.predict(img.reshape(1, 28, 28)).tolist()[0]
    p = None
    for i in range(10):
        if prediction[i] > 0.5:
            p = i
    return p


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def infer_image():
    # Catch the image file from a POST request
    if 'file' not in request.files:
        return "Please try again. The Image doesn't exist"

    file = request.files.get('file')

    if not file:
        return

    img = Image.open(request.files['file'].stream)

    # Prepare image - format to model
    img = image_processing(img)
    img.show()
    # Prepare the image - change format to read by computer
    img = prepare_image(img)


    # Return on a JSON format
    return jsonify(prediction=predict_result(img))


@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

