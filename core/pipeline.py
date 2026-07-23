import time

from preprocessing.preprocess import Preprocessor

from core.image_manager import ImageManager
from core.detector import DamageDetector
from core.result import ProcessingResult


class ProcessingPipeline:

    def __init__(self):

        self.images = ImageManager()

        self.detector = DamageDetector()

        self.preprocessor = Preprocessor()

    def process(self, path):

        result = ProcessingResult()

        start = time.time()

        # Load image
        original = self.images.load(path)

        result.original = original

        # Preprocessing
        pre = self.preprocessor.process(
            original.copy()
        )

        result.preprocessed = pre.processed

        # (Store preprocessing report for future UI)
        result.preprocessing = pre

        # Detection (placeholder)
        result.detected = self.detector.detect(
            result.preprocessed.copy()
        )

        # Processing time
        result.processing_time = round(
            time.time() - start,
            3
        )

        # Placeholder values
        result.damage_type = "Pending YOLO"
        result.confidence = "0%"
        result.severity = "Unknown"

        result.success = True
        result.message = "Processing Complete"

        return result