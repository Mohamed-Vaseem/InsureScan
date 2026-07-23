from ultralytics import YOLO
import cv2

from config import Settings
from preprocessing.cropper import VehicleCropper
from detection.vehicle_result import VehicleResult


class VehicleDetector:
    """
    Detects the primary vehicle in an image.
    """

    VEHICLE_CLASSES = {
        "car",
        "truck",
        "bus",
        "motorcycle"
    }

    def __init__(self):

        self.model = YOLO(Settings.VEHICLE_MODEL)

        self.cropper = VehicleCropper()

    def predict(self, image):

        result = VehicleResult()

        predictions = self.model.predict(

            source=image,

            conf=Settings.VEHICLE_CONFIDENCE,

            iou=Settings.VEHICLE_IOU,

            verbose=False
        )

        if len(predictions) == 0:

            result.message = "No predictions."

            return result

        prediction = predictions[0]

        annotated = prediction.plot()

        largest_area = 0

        best_box = None

        best_name = ""

        best_conf = 0.0

        names = self.model.names

        for box in prediction.boxes:

            cls = int(box.cls[0])

            name = names[cls]

            if name not in self.VEHICLE_CLASSES:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            area = (x2 - x1) * (y2 - y1)

            if area > largest_area:

                largest_area = area

                best_box = (x1, y1, x2, y2)

                best_name = name

                best_conf = float(box.conf[0])

        if best_box is None:

            result.message = "No vehicle detected."

            return result

        cropped = self.cropper.crop(image, best_box)

        result.success = True

        result.detected = True

        result.message = "Vehicle detected."

        result.class_name = best_name

        result.confidence = best_conf

        result.bounding_box = best_box

        result.cropped_image = cropped

        result.annotated_image = annotated

        return result