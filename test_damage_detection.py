from __future__ import annotations

from pathlib import Path

from ultralytics import YOLO


def main() -> None:
    project_root = Path(__file__).resolve().parent
    weights_path = project_root / "models" / "weights" / "damage_detection" / "yolo11n_damage" / "weights" / "best.pt"
    source_dir = project_root / "datasets_yolo" / "val" / "images"
    runs_root = project_root / "models" / "weights" / "damage_detection" / "predictions"

    model = YOLO(str(weights_path))
    results = model.predict(
        source=str(source_dir),
        conf=0.25,
        save=True,
        project=str(runs_root),
        name="yolo11n_damage_val",
        exist_ok=True,
    )

    save_dir = Path(results[0].save_dir) if results else runs_root / "yolo11n_damage_val"
    print("Prediction summary")
    print(f"Model: {weights_path}")
    print(f"Source images: {source_dir}")
    print(f"Saved predictions: {save_dir}")


if __name__ == "__main__":
    main()