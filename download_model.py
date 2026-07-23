from ultralytics import YOLO

# Downloads automatically if not already cached
model = YOLO("yolo11n.pt")

print("Model downloaded successfully!")