from preprocessing.preprocessing_result import PreprocessingResult
from preprocessing.analyzer import ImageAnalyzer

from preprocessing.gamma import gamma_correction
from preprocessing.clahe import apply_clahe
from preprocessing.resize import resize_image


class Preprocessor:
    """
    Executes preprocessing based on the
    recommendations produced by ImageAnalyzer.
    """

    def __init__(self):

        self.analyzer = ImageAnalyzer()

    def process(self, image):

        result = PreprocessingResult()

        result.original = image.copy()

        processed = image.copy()

        # -----------------------------------
        # Analyse image
        # -----------------------------------

        analysis = self.analyzer.analyze(processed)

        result.analysis = analysis

        # -----------------------------------
        # Apply preprocessing
        # -----------------------------------

        if analysis.need_gamma:

            processed = gamma_correction(processed)

        if analysis.need_clahe:

            processed = apply_clahe(processed)

        if analysis.need_resize:

            processed = resize_image(processed)

        # -----------------------------------
        # Normalization
        # -----------------------------------


        result.processed = processed

        result.success = True

        result.message = "Preprocessing completed."

        return result