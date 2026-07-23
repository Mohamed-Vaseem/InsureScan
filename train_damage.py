from ultralytics import YOLO


def main():

    model = YOLO("yolo11n-seg.pt")

    model.train(
        # Dataset
        data="datasets/damage_dataset/data.yaml",

        # Image size
        imgsz=640,

        # Training
        epochs=80,
        batch=8,

        # Hardware
        device=0,
        workers=4,

        # Performance
        cache="disk",
        pretrained=True,
        amp=True,

        # Early stopping
        patience=15,

        # Output
        project="training",
        name="damage_segmentation",
        save=True,
        save_period=10,
        plots=True,
        verbose=True
    )


if __name__ == "__main__":
    main()