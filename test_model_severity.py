from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")

model.train(
    data="datasets/severity_dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=8,
    device=0,
    project="training",
    name="severity_segmentation",
    cache=True,
    workers=4,
    patience=20
)