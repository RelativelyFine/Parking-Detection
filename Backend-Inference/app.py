from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from ultralytics import YOLO
import os
from threading import Lock

model = YOLO('top-down-park.pt')  # load a pretrained YOLOv8n classification model
lock = Lock()

app = Flask(__name__)
CORS(app)

@app.route("/parking", methods=["POST"])
@cross_origin()
def process_image():
    file = request.files['image']
    lock.acquire()
    # remove previous temp.png
    if os.path.exists('temp.png'):
        os.remove('temp.png')
    # save image to disk
    file.save('temp.png')
    results = model.predict(source='temp.png', save=True)
    last_dir = sorted(os.listdir('runs/detect'))[-1]
    lock.release()

    return send_file('runs/detect/' + last_dir + '/temp.png', mimetype='image/png')

@app.route('/upload', methods = ['POST'])
def upload_file():
    file = request.files['file']
    lock.acquire()
    # remove previous temp.png
    if os.path.exists('temp.png'):
        os.remove('temp.png')
    # save image to disk
    file.save('temp.png')
    results = model.predict(source='temp.png', save=True)
    last_dir = sorted(os.listdir('runs/detect'))[-1]
    lock.release()
    print("done!!!!!!!!!!!!!!!!!!!!!")
    return send_file('runs/detect/' + last_dir + '/temp.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
