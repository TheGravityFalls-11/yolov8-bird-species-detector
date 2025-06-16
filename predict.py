from ultralytics import YOLO

# Load your trained model (corrected path)
model = YOLO("C:/Users/ASUS/runs/detect/train3/weights/best.pt")



# Inference on a new image (make sure test.jpg exists in same directory)
results = model.predict("test4.jpg", save=True, imgsz=640)

# (Optional) print results summary
for r in results:
    print(r)
