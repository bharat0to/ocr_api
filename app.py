from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
import os, logging
import time
from utils import get_file_name


UPLOAD_FOLDER = os.path.realpath('uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__)
cors = CORS(app)
logging.basicConfig(
    filename='debug.logs', 
    level=logging.DEBUG,
    format="%(levelname)s %(created)f %(message)s"
)

def debug_log(image, size, rt, tt):
    ip = request.environ['REMOTE_ADDR']
    logging.debug(f"{ip} {rt:.4f} {tt-rt:.4f} {tt:.4f} {size/1024:.4f} {image}")


@app.route('/scan', methods=['POST'])
def scan():
    tic = time.time()
    if 'image' in request.files:
        image_fs = request.files['image']
        image_file = get_file_name(image_fs.filename)
        try:
            # convert image to textw
            image_fs.save(image_file)
            rt = time.time() - tic
            text = pytesseract.image_to_string(image_file)
            tt = time.time() - tic

            size = os.stat(image_file).st_size
            debug_log(image_file, size, rt, tt)
            return jsonify({ 'text': text })
        except Exception as e:
            logging.error(e)
            # log return 500
            return jsonify({"error": "Internal server error"}), 500
    else:
        return jsonify({"error": "data is required"}), 400

if __name__ == '__main__':
    app.run()