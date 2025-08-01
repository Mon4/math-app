import os
from flask import Flask, jsonify, request
from extractDigits import *


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def infer_image():
    # sprawdzenie czy przekazano plik z obrazem
    if 'file' not in request.files:
        return "Please try again. The Image doesn't exist"

    # zapisanie obrazu na serwerze w celu sprawdzenia jak wygląda otrzymywany obraz
    file = request.files.get('file')
    file.save(os.path.join(app.root_path, 'static/image.png'))

    if not file:
        return

    # odczyt obrazu i przekazanie go do funkcji dzielącej liczby na cyfry,
    # a następnie do funkcji wykorzystującej model do rozpoznawania cyfr
    img = Image.open(request.files['file'].stream)
    img = np.array(img)
    result = extract_digits(img)

    return jsonify(result)  # zwrócenie wyniku w formacie JSON


@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning'


# uruchomienie aplikacji Flask na lokalnym serwerze
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
