import time

from core.image_manager import ImageManager
from core.input_manager import InputManager

from detection.damage_detector import DamageDetector

from core.result import ProcessingResult


class ProcessingPipeline:

    """
    Main InsureScan AI Pipeline.
    """

    def __init__(self):

        self.images = ImageManager()

        self.input = InputManager()

        self.detector = DamageDetector()

    def process(self, path):

        start = time.time()

        result = ProcessingResult()

        # -------------------------
        # Load Image
        # -------------------------

        image = self.images.load(path)

        # -------------------------
        # Input Stage
        # -------------------------

        input_result = self.input.prepare(image)

        result.input = input_result

        result.original = input_result.original

        if input_result.cropped is not None:

            result.cropped = input_result.cropped

        if input_result.processed is not None:

            result.preprocessed = input_result.processed

        if not input_result.success:

            result.message = input_result.message

            return result

        # -------------------------
        # Damage Detection
        # -------------------------

        damage = self.detector.detect(
            input_result.processed
        )

        result.damage = damage

        result.detected = damage

        # -------------------------
        # Placeholder
        # -------------------------

        result.damage_type = "Pending YOLO11-Seg"

        result.confidence = "--"

        result.severity = "--"

        # -------------------------
        # Finish
        # -------------------------

        result.processing_time = round(
            time.time() - start,
            3
        )

        result.success = True

        result.message = "Pipeline completed."

        return result