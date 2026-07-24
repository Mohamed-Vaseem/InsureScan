import time

from core.image_manager import ImageManager
from core.input_manager import InputManager
from core.processing_result import ProcessingResult

from detection.damage_detector import DamageDetector
from detection.part_detector import PartDetector


class ProcessingPipeline:
    """
    Main InsureScan pipeline.
    """

    def __init__(self):

        self.image_manager = ImageManager()

        self.input_manager = InputManager()

        self.damage_detector = DamageDetector()

        self.part_detector = PartDetector()

    def process(self, image_path):

        start = time.time()

        result = ProcessingResult()

        try:

            # -----------------------
            # Load Image
            # -----------------------

            image = self.image_manager.load(image_path)

            # -----------------------
            # Input Pipeline
            # -----------------------

            input_result = self.input_manager.prepare(image)

            result.input = input_result

            result.original = input_result.original

            result.cropped = input_result.cropped

            result.preprocessed = input_result.processed

            if not input_result.success:

                result.message = input_result.message

                return result

            # -----------------------
            # Damage Detection
            # -----------------------

            damage = self.damage_detector.predict(
                input_result.processed
            )

            result.damage = damage

            if damage.success:
                result.segmented = damage.annotated_image

            # -----------------------
            # Part Detection
            # -----------------------

            part = self.part_detector.predict(
                input_result.processed
            )

            result.part = part

            if part.success:
                result.part_segmented = part.annotated_image

            # -----------------------

            result.processing_time = round(
                time.time() - start,
                3
            )

            result.success = True

            result.message = "Pipeline completed."

            return result

        except Exception as e:

            result.success = False

            result.message = str(e)

            return result