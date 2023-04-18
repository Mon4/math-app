import os
from flask import Flask, jsonify, request
from extractDigits import *


def prepare_image(img):
    img = np.array(img)
    return img


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
    img = np.array(img)  # cast from Image to (cv2) img
    result = extractDigits(img)

    return jsonify(result)  # Return a JSON format


@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

