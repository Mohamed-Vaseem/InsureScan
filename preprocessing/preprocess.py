from config import Settings

from preprocessing.analyzer import ImageAnalyzer
from preprocessing.preprocessing_result import PreprocessingResult

from preprocessing.filters.gamma import gamma_correction
from preprocessing.filters.clahe import apply_clahe

from preprocessing.resize import resize_image
from preprocessing.normalize import normalize


class Preprocessor:

    """
    Safe preprocessing.

    Goal:
    Preserve vehicle damage while making
    the image suitable for AI inference.
    """

    def __init__(self):

        self.analyzer = ImageAnalyzer()

    def process(self, image):

        result = PreprocessingResult()

        result.original = image.copy()

        analysis = self.analyzer.analyze(image)

        result.analysis = analysis

        processed = image.copy()

        # -------------------------
        # Brightness
        # -------------------------

        if analysis.brightness < Settings.MIN_BRIGHTNESS:

            processed = gamma_correction(processed)

            result.operations.append(
                "Gamma Correction"
            )

        # -------------------------
        # Contrast
        # -------------------------

        if analysis.contrast < Settings.MIN_CONTRAST:

            processed = apply_clahe(processed)

            result.operations.append(
                "CLAHE"
            )

        # -------------------------
        # Resize
        # -------------------------

        processed = resize_image(processed)

        result.operations.append("Resize")

        # -------------------------
        # Normalize
        # -------------------------

        processed = normalize(processed)

        result.operations.append("Normalize")

        result.processed = processed

        return result