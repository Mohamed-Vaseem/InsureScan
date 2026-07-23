from ultralytics import YOLO


def main():

    model = YOLO("yolo11n-seg.pt")

    model.train(
        data="datasets/damage_dataset/data.yaml",

        epochs=50,
        imgsz=640,

        batch=8,
        workers=4,

        device=0,

        cache=True,#cache="disk"
        pretrained=True,

        project="training",
        name="damage_segmentation",

        patience=20,
        save=True,
        verbose=True
    )


if __name__ == "__main__":
    main()