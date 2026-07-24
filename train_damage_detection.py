from __future__ import annotations

from pathlib import Path

from ultralytics import YOLO


def main() -> None:
    project_root = Path(__file__).resolve().parent
    data_yaml = project_root / "datasets_yolo" / "data.yaml"
    weights_root = project_root / "models" / "weights" / "damage_detection"
    weights_root.mkdir(parents=True, exist_ok=True)

    model = YOLO("yolo11n.pt")

    train_results = model.train(
        data=str(data_yaml),
        epochs=50,
        imgsz=640,
        batch=8,
        pretrained=True,
        project=str(weights_root),
        name="yolo11n_damage",
        exist_ok=True,
    )

    best_weights = Path(train_results.save_dir) / "weights" / "best.pt"
    metrics = model.val(data=str(data_yaml), imgsz=640, batch=8, conf=0.001, iou=0.6)

    precision = float(metrics.box.mp)
    recall = float(metrics.box.mr)
    map50 = float(metrics.box.map50)

    print("Training summary")
    print(f"Data: {data_yaml}")
    print(f"Best weights: {best_weights}")
    print(f"mAP50: {map50:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")


if __name__ == "__main__":
    main()