from ultralytics import YOLO

model = YOLO("models/damage/best.pt")

print("Model loaded successfully!")
print("Classes:", model.names)