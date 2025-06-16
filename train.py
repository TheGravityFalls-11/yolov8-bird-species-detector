from ultralytics import YOLO

# Load pretrained YOLOv8 model (smallest model yolov8n.pt)
model = YOLO("yolov8n.pt")

# Start training
model.train(data="data.yaml", epochs=25, imgsz=640)

# Optional evaluation
model.val()
