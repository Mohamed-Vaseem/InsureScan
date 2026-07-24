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


def convert_bbox_to_yolo(bbox: list[float], image_width: int, image_height: int) -> tuple[float, float, float, float]:
    x, y, width, height = bbox
    center_x = (x + width / 2.0) / image_width
    center_y = (y + height / 2.0) / image_height
    norm_width = width / image_width
    norm_height = height / image_height
    return center_x, center_y, norm_width, norm_height


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


def convert_split(split_name: str, source_dir: Path, annotation_path: Path, output_root: Path) -> SplitSummary:
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

            x_center, y_center, box_width, box_height = convert_bbox_to_yolo(
                annotation["bbox"], image["width"], image["height"]
            )
            label_lines.append(
                f"0 {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}"
            )
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert damage COCO annotations to YOLO detection format.")
    parser.add_argument(
        "--source-root",
        type=Path,
        default=Path("datasets"),
        help="Source dataset root containing train/val folders and COCO JSON files.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("datasets_yolo"),
        help="Output root for the YOLO dataset.",
    )
    args = parser.parse_args()

    source_root: Path = args.source_root
    output_root: Path = args.output_root

    train_summary = convert_split(
        "train",
        source_root / "train",
        source_root / "train" / "COCO_train_annos.json",
        output_root,
    )
    val_summary = convert_split(
        "val",
        source_root / "val",
        source_root / "val" / "COCO_val_annos.json",
        output_root,
    )

    output_root.mkdir(parents=True, exist_ok=True)
    write_data_yaml(output_root)

    train_images, train_labels, train_missing = verify_split(output_root, "train")
    val_images, val_labels, val_missing = verify_split(output_root, "val")

    print("Conversion summary")
    print(f"Output root: {output_root.resolve()}")
    print(f"Classes: 1 -> damage")
    print(
        f"Train: {train_summary.images_copied}/{train_summary.images_total} images copied, "
        f"{train_summary.labels_written} labels written, {train_summary.annotations_written} annotations converted, "
        f"{train_summary.missing_source_images} missing source images"
    )
    print(
        f"Val: {val_summary.images_copied}/{val_summary.images_total} images copied, "
        f"{val_summary.labels_written} labels written, {val_summary.annotations_written} annotations converted, "
        f"{val_summary.missing_source_images} missing source images"
    )
    print(
        f"Verification: train images={train_images}, train labels={train_labels}, train missing labels={train_missing}; "
        f"val images={val_images}, val labels={val_labels}, val missing labels={val_missing}"
    )

    if train_missing or val_missing:
        raise SystemExit("Conversion finished with missing label files.")


if __name__ == "__main__":
    main()