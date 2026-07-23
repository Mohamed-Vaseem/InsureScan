from pathlib import Path

# Old class ID -> New class ID
CLASS_MAP = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 0,
    9: 1,
    10: 2,
    11: 3,
    12: 4,
    13: 5,
    14: 6,
    15: 7,
}

folders = [
    "datasets/damage_dataset/train/labels",
    "datasets/damage_dataset/valid/labels",
    "datasets/damage_dataset/test/labels",
]

for folder in folders:

    folder = Path(folder)

    for txt in folder.glob("*.txt"):

        if txt.stat().st_size == 0:
            continue

        new_lines = []

        with open(txt, "r") as f:

            for line in f.readlines():

                parts = line.strip().split()

                if not parts:
                    continue

                old_class = int(parts[0])

                parts[0] = str(CLASS_MAP[old_class])

                new_lines.append(" ".join(parts))

        with open(txt, "w") as f:
            f.write("\n".join(new_lines))

print("Dataset cleaned successfully!")