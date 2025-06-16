# 🦉 Bird Species Detector using YOLOv8

This project detects various bird species using a YOLOv8 object detection model. Dataset is annotated via Roboflow and contains multiple bird classes.

## 📁 Folder Structure

```
ACM TASK3/
│
├── train/
│   ├── images/
│   └── labels/
├── data.yaml
├── train.py
├── predict.py
├── yolov8n.pt
├── test.jpg
├── test2.jpg
├── test3.jpg
├── test4.jpg
└── README.md
```

## 🚀 Features

- YOLOv8-based object detection
- Roboflow-annotated dataset
- Inference and Training scripts
- 14 bird species detection

## 📸 Sample Detection Output

Here is an example of how the YOLOv8 detection looks:



![Prediction Screenshot](f1b0df61-5aa0-400b-9835-3a0df7b6062c.png)

---

## 🛠️ How to Train

```bash
python train.py
```

Make sure `data.yaml` is properly configured.

---

## 🔍 How to Predict

```bash
python predict.py
```

Make sure `predict.py` loads your trained model and points to a test image.

---

## 📦 Model Info

- Model used: `yolov8n.pt`
- Framework: Ultralytics YOLOv8
- Python version: 3.12+
- Torch CPU

---

## 🤝 Contributing

Feel free to fork and raise a PR! Star ⭐ the repo if you like it!

