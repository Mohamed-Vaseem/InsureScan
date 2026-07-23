from core.input_result import InputResult

from preprocessing.validator import ImageValidator
from preprocessing.preprocess import Preprocessor

from detection.vehicle_detector import VehicleDetector


class InputManager:
    """
    Responsible for preparing an image
    before damage detection.
    """

    def __init__(self):

        self.validator = ImageValidator()

        self.vehicle_detector = VehicleDetector()

        self.preprocessor = Preprocessor()

    def prepare(self, image):

        result = InputResult()

        # -----------------------
        # Original Image
        # -----------------------

        result.original = image.copy()

        # -----------------------
        # Validation
        # -----------------------

        validation = self.validator.validate(image)

        result.validation = validation

        if not validation.is_valid:

            result.message = "Image validation failed."

            return result

        # -----------------------
        # Vehicle Detection
        # -----------------------

        vehicle = self.vehicle_detector.predict(image)

        result.vehicle = vehicle

        if not vehicle.success:

            result.message = vehicle.message

            return result

        cropped = vehicle.cropped_image

        result.cropped = cropped

        preprocessing = self.preprocessor.process(cropped)

        result.preprocessing = preprocessing

        result.processed = preprocessing.processed

        result.success = True

        result.message = "Input preparation completed."

        return result

        # -----------------------
        # Preprocessing
        # -----------------------

        preprocessing = self.preprocessor.process(
            vehicle.cropped_image
        )

        result.preprocessing = preprocessing

        result.processed = preprocessing.processed

        result.success = True

        result.message = "Input prepared successfully."

        return result