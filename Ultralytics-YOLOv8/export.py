from ultralytics import YOLO

model = YOLO("runs/detect/train27/weights/best.pt")
model.fuse()  
model.info(verbose=True)  # Print model information
model.export(format="onnx")  # Export to ONNX format