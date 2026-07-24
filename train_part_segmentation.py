from ultralytics import YOLO

def main():
    model = YOLO("yolo11n-seg.pt")

    model.train(
        data="datasets/part_dataset/data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        device=0,
        project="training",
        name="part_segmentation",
        cache=True,
    )

if __name__ == "__main__":
    main()