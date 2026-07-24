from pathlib import Path
from ultralytics import YOLO

model = YOLO("models/damage/best.pt")

image = Path("test_images") / "car1.jpg"

results = model.predict(
    source=str(image),
    save=True,
    conf=0.35
)

print("Results:", results)