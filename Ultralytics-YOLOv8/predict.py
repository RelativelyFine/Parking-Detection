from ultralytics import YOLO
from matplotlib import pyplot as plt
model = YOLO('runs/detect/train27/weights/best.pt')  # load a pretrained YOLOv8n classification model
tensor_image = model('image22.png', show=True)  # predict on an image