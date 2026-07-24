from ultralytics import YOLO

def main():

    model = YOLO("yolo11n-seg.pt")

    model.train(
        data="datasets/part_dataset/data.yaml",
        epochs=100,
        imgsz=640,
        batch=8,
        device=0,
        project="training",
        name="part_segmentation_v2",
        cache=True,
        workers=4,
        patience=20
    )

if __name__ == "__main__":
    main()