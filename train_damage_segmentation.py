from __future__ import annotations

from pathlib import Path

from ultralytics import YOLO


def main() -> None:
    project_root = Path(__file__).resolve().parent
    data_yaml = project_root / "datasets_yolo_seg" / "data.yaml"
    weights_root = project_root / "models" / "weights" / "damage_segmentation"
    weights_root.mkdir(parents=True, exist_ok=True)

    model = YOLO("yolo11n-seg.pt")

    train_results = model.train(
        data=str(data_yaml),
        epochs=50,
        imgsz=640,
        batch=8,
        pretrained=True,
        project=str(weights_root),
        name="yolo11n_damage_seg",
        exist_ok=True,
    )

    best_weights = Path(train_results.save_dir) / "weights" / "best.pt"
    metrics = model.val(data=str(data_yaml), imgsz=640, batch=8, conf=0.001, iou=0.6)

    box_precision = float(metrics.box.mp)
    box_recall = float(metrics.box.mr)
    box_map50 = float(metrics.box.map50)
    mask_precision = float(metrics.seg.mp)
    mask_recall = float(metrics.seg.mr)
    mask_map50 = float(metrics.seg.map50)

    print("Segmentation training summary")
    print(f"Data: {data_yaml}")
    print(f"Best weights: {best_weights}")
    print(f"Box Precision: {box_precision:.4f}")
    print(f"Box Recall: {box_recall:.4f}")
    print(f"Box mAP50: {box_map50:.4f}")
    print(f"Mask Precision: {mask_precision:.4f}")
    print(f"Mask Recall: {mask_recall:.4f}")
    print(f"Mask mAP50: {mask_map50:.4f}")


if __name__ == "__main__":
    main()