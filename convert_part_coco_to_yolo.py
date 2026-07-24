import json
from pathlib import Path

# ------------------------------------
# CHANGE ONLY THESE PATHS IF REQUIRED
# ------------------------------------

DATASET = Path("datasets/part_dataset")

SETS = [
    ("train", "COCO_mul_train_annos.json"),
    ("val", "COCO_mul_val_annos.json"),
]

# ------------------------------------


def convert(split, json_name):
    json_path = DATASET / split / json_name

    with open(json_path, "r") as f:
        coco = json.load(f)

    images = {img["id"]: img for img in coco["images"]}

    labels = {}

    for ann in coco["annotations"]:

        img = images[ann["image_id"]]

        w = img["width"]
        h = img["height"]

        file = Path(img["file_name"]).stem + ".txt"

        cls = ann["category_id"] - 1

        line = [str(cls)]

        seg = ann["segmentation"][0]

        for i in range(0, len(seg), 2):
            x = seg[i] / w
            y = seg[i + 1] / h

            line.append(f"{x:.6f}")
            line.append(f"{y:.6f}")

        labels.setdefault(file, []).append(" ".join(line))

    label_dir = DATASET / split / "labels"
    label_dir.mkdir(exist_ok=True)

    for file, lines in labels.items():
        with open(label_dir / file, "w") as f:
            f.write("\n".join(lines))

    print(split, "Done.")


for split, js in SETS:
    convert(split, js)

print("Finished.")