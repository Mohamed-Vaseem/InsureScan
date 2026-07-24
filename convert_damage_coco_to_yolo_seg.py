from __future__ import annotations

import argparse
import json
import shutil
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass
class SplitSummary:
    images_total: int = 0
    images_copied: int = 0
    labels_written: int = 0
    annotations_written: int = 0
    missing_source_images: int = 0
    skipped_annotations: int = 0


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def normalize_polygon(polygon: list[float], image_width: int, image_height: int) -> list[float]:
    normalized: list[float] = []
    for index, point in enumerate(polygon):
        if index % 2 == 0:
            normalized.append(clamp01(point / image_width))
        else:
            normalized.append(clamp01(point / image_height))
    return normalized


def load_coco_annotations(annotation_path: Path) -> tuple[dict[int, dict], dict[int, list[dict]]]:
    with annotation_path.open("r", encoding="utf-8") as file_handle:
        coco = json.load(file_handle)

    images_by_id = {image["id"]: image for image in coco.get("images", [])}
    annotations_by_image_id: dict[int, list[dict]] = defaultdict(list)
    for annotation in coco.get("annotations", []):
        annotations_by_image_id[annotation["image_id"]].append(annotation)

    return images_by_id, annotations_by_image_id


def write_data_yaml(output_root: Path) -> None:
    data_yaml = "\n".join(
        [
            f"path: {output_root.as_posix()}",
            "train: train/images",
            "val: val/images",
            "nc: 1",
            "names:",
            "  - damage",
            "",
        ]
    )
    (output_root / "data.yaml").write_text(data_yaml, encoding="utf-8")


def convert_segmentation_split(split_name: str, source_dir: Path, annotation_path: Path, output_root: Path) -> SplitSummary:
    images_by_id, annotations_by_image_id = load_coco_annotations(annotation_path)
    output_images_dir = output_root / split_name / "images"
    output_labels_dir = output_root / split_name / "labels"
    output_images_dir.mkdir(parents=True, exist_ok=True)
    output_labels_dir.mkdir(parents=True, exist_ok=True)

    summary = SplitSummary(images_total=len(images_by_id))

    for image in images_by_id.values():
        source_image_path = source_dir / image["file_name"]
        target_image_path = output_images_dir / image["file_name"]
        target_label_path = output_labels_dir / f"{Path(image['file_name']).stem}.txt"

        if not source_image_path.exists():
            summary.missing_source_images += 1
            continue

        shutil.copy2(source_image_path, target_image_path)
        summary.images_copied += 1

        label_lines: list[str] = []
        for annotation in annotations_by_image_id.get(image["id"], []):
            if annotation.get("category_id") != 1:
                continue
            if annotation.get("iscrowd", 0) == 1:
                summary.skipped_annotations += 1
                continue

            segmentation = annotation.get("segmentation", [])
            if not isinstance(segmentation, list):
                summary.skipped_annotations += 1
                continue

            polygons = segmentation if segmentation and isinstance(segmentation[0], list) else [segmentation]
            for polygon in polygons:
                if not polygon or len(polygon) < 6 or len(polygon) % 2 != 0:
                    summary.skipped_annotations += 1
                    continue

                normalized_polygon = normalize_polygon(polygon, image["width"], image["height"])
                polygon_values = " ".join(f"{value:.6f}" for value in normalized_polygon)
                label_lines.append(f"0 {polygon_values}")
                summary.annotations_written += 1

        target_label_path.write_text("\n".join(label_lines) + ("\n" if label_lines else ""), encoding="utf-8")
        summary.labels_written += 1

    return summary


def verify_split(output_root: Path, split_name: str) -> tuple[int, int, int]:
    images_dir = output_root / split_name / "images"
    labels_dir = output_root / split_name / "labels"

    image_files = [path for path in images_dir.iterdir() if path.is_file()]
    label_files = [path for path in labels_dir.iterdir() if path.is_file() and path.suffix == ".txt"]

    missing_labels = 0
    for image_path in image_files:
        label_path = labels_dir / f"{image_path.stem}.txt"
        if not label_path.exists():
            missing_labels += 1

    return len(image_files), len(label_files), missing_labels


def collect_sample_label_lines(output_root: Path, limit: int = 5) -> list[str]:
    samples: list[str] = []
    for split_name in ("train", "val"):
        labels_dir = output_root / split_name / "labels"
        if not labels_dir.exists():
            continue
        for label_path in sorted(labels_dir.glob("*.txt")):
            lines = [line.strip() for line in label_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            for line in lines:
                samples.append(f"{split_name}/{label_path.name}: {line}")
                if len(samples) >= limit:
                    return samples
    return samples


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert damage COCO instance segmentation annotations to YOLOv11 segmentation format.")
    parser.add_argument(
        "--source-root",
        type=Path,
        default=Path("datasets"),
        help="Source dataset root containing train/val folders and COCO JSON files.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("datasets_yolo_seg"),
        help="Output root for the YOLO segmentation dataset.",
    )
    args = parser.parse_args()

    source_root: Path = args.source_root
    output_root: Path = args.output_root
    output_root.mkdir(parents=True, exist_ok=True)

    train_summary = convert_segmentation_split(
        "train",
        source_root / "train",
        source_root / "train" / "COCO_train_annos.json",
        output_root,
    )
    val_summary = convert_segmentation_split(
        "val",
        source_root / "val",
        source_root / "val" / "COCO_val_annos.json",
        output_root,
    )

    write_data_yaml(output_root)

    train_images, train_labels, train_missing = verify_split(output_root, "train")
    val_images, val_labels, val_missing = verify_split(output_root, "val")
    total_labels = train_labels + val_labels
    missing_labels = train_missing + val_missing
    sample_lines = collect_sample_label_lines(output_root)

    print("Segmentation conversion summary")
    print(f"Output root: {output_root.resolve()}")
    print("Class mapping: 0 -> damage")
    print(f"Training images: {train_images}")
    print(f"Validation images: {val_images}")
    print(f"Labels: {total_labels}")
    print(f"Missing labels: {missing_labels}")
    print(
        f"Train split: copied {train_summary.images_copied}/{train_summary.images_total} images, "
        f"wrote {train_summary.labels_written} labels, converted {train_summary.annotations_written} polygons, "
        f"skipped {train_summary.skipped_annotations} annotations"
    )
    print(
        f"Val split: copied {val_summary.images_copied}/{val_summary.images_total} images, "
        f"wrote {val_summary.labels_written} labels, converted {val_summary.annotations_written} polygons, "
        f"skipped {val_summary.skipped_annotations} annotations"
    )
    print("Sample label lines:")
    for line in sample_lines:
        print(f"  {line}")

    if missing_labels:
        raise SystemExit("Conversion finished with missing label files.")


if __name__ == "__main__":
    main()