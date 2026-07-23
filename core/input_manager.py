from preprocessing.validator import ImageValidator
from preprocessing.preprocess import Preprocessor

from detection.vehicle_detector import VehicleDetector


class InputManager:

    """
    Responsible for preparing an image
    before AI damage detection.

    Pipeline

    Validate

    ↓

    Detect Vehicle

    ↓

    Crop Vehicle

    ↓

    Preprocess

    """

    def __init__(self):

        self.validator = ImageValidator()

        self.detector = VehicleDetector()

        self.preprocessor = Preprocessor()

    def prepare(self, image):

        from core.input_result import InputResult

        result = InputResult()

        result.original = image.copy()

        # -------------------------
        # Validation
        # -------------------------

        validation = self.validator.validate(image)

        result.validation = validation

        if not validation.is_valid:

            result.message = "Image validation failed."

            return result

        # -------------------------
        # Vehicle Detection
        # -------------------------

        vehicle = self.detector.detect(image)

        result.vehicle = vehicle

        if not vehicle.found:

            result.message = "No vehicle detected."

            return result

        result.cropped = vehicle.cropped_image

        # -------------------------
        # Preprocessing
        # -------------------------

        pre = self.preprocessor.process(
            vehicle.cropped_image
        )

        result.preprocessing = pre

        result.processed = pre.processed

        result.success = True

        result.message = "Input ready."

        return result