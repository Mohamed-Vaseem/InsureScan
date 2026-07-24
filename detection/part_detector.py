import numpy as np
from ultralytics import YOLO

from config.settings import Settings
from detection.damage_result import DamageResult
from detection.damage_detection import DamageDetection


class PartDetector:
    """
    YOLO11-Seg vehicle part detector.
    """

    def __init__(self):
        self.model = YOLO(Settings.PART_MODEL)

    def predict(self, image):

        result = DamageResult()

        predictions = self.model.predict(
            source=image,
            conf=0.35,
            verbose=False
        )

        prediction = predictions[0]

        annotated = prediction.plot()

        boxes = prediction.boxes
        masks = prediction.masks

        if boxes is None or len(boxes) == 0:
            result.success = True
            result.message = "No parts detected."
            result.annotated_image = annotated
            return result

        for i in range(len(boxes)):

            detection = DamageDetection()

            box = boxes[i]

            detection.class_id = int(box.cls.item())
            detection.class_name = self.model.names[detection.class_id]
            detection.confidence = float(box.conf.item())

            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

            detection.bounding_box = (
                int(x1),
                int(y1),
                int(x2),
                int(y2)
            )

            if masks is not None:
                mask = masks.data[i].cpu().numpy()

                detection.mask = mask
                detection.polygon = masks.xy[i]
                detection.area = int(np.count_nonzero(mask))

            result.detections.append(detection)

        result.annotated_image = annotated
        result.success = True
        result.message = f"{result.count} part(s) detected."

        return result