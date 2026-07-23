import time

from ultralytics import YOLO

from preprocessing.cropper import Cropper

from detection.vehicle_result import VehicleResult

from config import Settings


class VehicleDetector:

    """
    Detects the primary vehicle
    inside an image using YOLO11.
    """

    def __init__(self):

        self.model = YOLO(
            "models/vehicle/yolo11n.pt"
        )

    def detect(self, image):

        start = time.time()

        result = VehicleResult()

        predictions = self.model.predict(
            image,
            verbose=False
        )

        boxes = predictions[0].boxes

        if len(boxes) == 0:

            result.processing_time = round(
                time.time() - start,
                3
            )

            return result

        best = None
        best_conf = 0

        for box in boxes:

            cls = int(box.cls.item())

            name = self.model.names[cls]

            # COCO vehicle classes
            if name not in [
                "car",
                "truck",
                "bus"
            ]:
                continue

            conf = float(box.conf.item())

            if conf > best_conf:

                best = box
                best_conf = conf

        if best is None:

            result.processing_time = round(
                time.time() - start,
                3
            )

            return result

        x1, y1, x2, y2 = map(
            int,
            best.xyxy[0]
        )

        result.bounding_box = (
            x1,
            y1,
            x2,
            y2
        )

        result.confidence = best_conf

        result.class_name = self.model.names[
            int(best.cls.item())
        ]

        result.margin = Settings.CROP_MARGIN

        result.cropped_image = Cropper.crop(
            image,
            result.bounding_box,
            Settings.CROP_MARGIN
        )

        result.found = True

        result.processing_time = round(
            time.time() - start,
            3
        )

        return result