from preprocessing.analyzer import ImageAnalyzer
from preprocessing.result import PreprocessingResult

from preprocessing.filters.gamma import gamma_correction
from preprocessing.filters.clahe import apply_clahe
from preprocessing.filters.denoise import remove_noise
from preprocessing.filters.bilateral import bilateral_filter
from preprocessing.filters.sharpen import sharpen

from preprocessing.resize import resize_image
from preprocessing.normalize import normalize
from preprocessing.quality import calculate_quality
from preprocessing.config import *

class Preprocessor:

    def __init__(self):

        self.analyzer = ImageAnalyzer()

    def process(self, image):

        result = PreprocessingResult()

        result.original = image.copy()

        report = self.analyzer.analyze(image)
        result.analysis = report

        result.quality_score = calculate_quality(report)

        result.blur_score = report["blur"]
        result.brightness = report["brightness"]
        result.contrast = report["contrast"]
        result.noise_score = report["noise"]
        result.sharpness = report["sharpness"]

        processed = image.copy()

        # Brightness
        if report["is_dark"]:
            processed = gamma_correction(processed)
            result.operations.append("Gamma Correction")
            result.is_dark = True

        # Contrast
        if report["low_contrast"]:
            processed = apply_clahe(processed)
            result.operations.append("CLAHE")
            result.low_contrast = True

        # Noise
        if report["is_noisy"]:

            processed = remove_noise(processed)

            processed = bilateral_filter(processed)

            result.operations.append("Noise Removal")
            result.operations.append("Bilateral Filter")

            result.is_noisy = True

        # Blur
        if report["blur"] < BLUR_LOW:

            result.warnings.append(
                "Image is heavily blurred."
            )

        elif report["blur"] < BLUR_MEDIUM:

            processed = sharpen(processed)

            result.operations.append("Sharpen")

            result.is_blurry = True

        # Preserve edges
        if report["is_noisy"]:

            processed = bilateral_filter(processed)

            result.operations.append("Bilateral Filter")

        if report["overexposure"] > 15:

            result.warnings.append(
                "Image contains overexposed regions."
            )
        # Resize
        processed = resize_image(processed)
        result.operations.append("Resize")

        # Normalize
        processed = normalize(processed)
        result.operations.append("Normalize")
        
        if len(result.operations) == 0:

            result.operations.append(
                "No preprocessing required"
            )

        result.processed = processed
        
        result.quality_score = calculate_quality(report)

        return result