import cv2

from detection.damage_result import DamageResult
from detection.damage_detection import DamageDetection


class DamageDetector:
    """
    Temporary mock detector.

    This class simulates YOLO11-Seg output so the
    UI can be developed before model training.
    """

    def __init__(self):
        pass

    def predict(self, image):

        result = DamageResult()

        annotated = image.copy()

        height, width = image.shape[:2]

        # Fake bounding box
        x1 = int(width * 0.30)
        y1 = int(height * 0.35)

        x2 = int(width * 0.65)
        y2 = int(height * 0.60)

        detection = DamageDetection()

        detection.class_id = 0
        detection.class_name = "Scratch"
        detection.confidence = 0.95
        detection.bounding_box = (x1, y1, x2, y2)
        detection.area = (x2 - x1) * (y2 - y1)

        # Draw fake detection
        cv2.rectangle(
            annotated,
            (x1, y1),
            (x2, y2),
            (0, 0, 255),
            2
        )

        cv2.putText(
            annotated,
            f"{detection.class_name} ({detection.confidence:.2f})",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

        result.annotated_image = annotated
        result.detections.append(detection)

        result.success = True
        result.message = "Mock detection completed."

        return result