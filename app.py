from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
import os, logging

UPLOAD_FOLDER = os.path.realpath('uploads')

app = Flask(__name__)
cors = CORS(app)
# logging.basicConfig(filename='logs.csv', level=logging.DEBUG)

@app.route('/scan', methods=['POST'])
def scan():
    image_fs = request.files['image']
    image_file = os.path.join(UPLOAD_FOLDER, image_fs.filename)
    image_fs.save(image_file)
    text = pytesseract.image_to_string(image_file)
    return jsonify({ 'text': text })
    # ip = request.environ['REMOTE_ADDR']
    # if 'data' in data:
    #     img64 = data['data']
    #     try:
    #         # convert image to text
    #         return jsonify({"text": "scanned text"})
    #     except:
    #         # log return 500
    #         return jsonify({"error": "Internal server error"})
    # else:
    #     return jsonify({"error": "data is required"}), 400

if __name__ == '__main__':
    app.run()