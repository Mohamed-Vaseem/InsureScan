import time

from preprocessing.preprocess import preprocess
from core.image_manager import ImageManager
from core.detector import DamageDetector
from core.result import ProcessingResult


class ProcessingPipeline:

    def __init__(self):
        self.images = ImageManager()
        self.detector = DamageDetector()

    def process(self, path):

        result = ProcessingResult()

        start = time.time()

        # Load Image
        original = self.images.load(path)
        result.original = original

        # Preprocess
        result.preprocessed = preprocess(
            original.copy()
        )

        # Detection (placeholder)
        result.detected = self.detector.detect(
            result.preprocessed.copy()
        )

        # Processing time
        result.processing_time = round(
            time.time() - start,
            3
        )

        # Temporary placeholder values
        result.damage_type = "Pending YOLO"
        result.confidence = "0%"
        result.severity = "Unknown"
        result.success = True
        result.message = "Processing Complete"

        return result