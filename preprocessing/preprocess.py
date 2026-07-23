from preprocessing.analyzer import ImageAnalyzer
from preprocessing.result import PreprocessingResult

from preprocessing.filters.gamma import gamma_correction
from preprocessing.filters.clahe import apply_clahe
from preprocessing.filters.denoise import remove_noise
from preprocessing.filters.bilateral import bilateral_filter
from preprocessing.filters.sharpen import sharpen

from preprocessing.resize import resize_image
from preprocessing.normalize import normalize


class Preprocessor:

    def __init__(self):

        self.analyzer = ImageAnalyzer()

    def process(self, image):

        result = PreprocessingResult()

        result.original = image.copy()

        report = self.analyzer.analyze(image)

        result.blur_score = report["blur"]
        result.brightness = report["brightness"]
        result.contrast = report["contrast"]
        result.noise_score = report["noise"]
        result.sharpness = report["sharpness"]

        processed = image.copy()

        # Brightness
        if report["brightness"] < 80:
            processed = gamma_correction(processed)
            result.operations.append("Gamma Correction")
            result.is_dark = True

        # Contrast
        if report["contrast"] < 40:
            processed = apply_clahe(processed)
            result.operations.append("CLAHE")
            result.low_contrast = True

        # Noise
        if report["noise"] > 20:
            processed = remove_noise(processed)
            result.operations.append("Noise Removal")
            result.is_noisy = True

        # Blur
        if report["blur"] < 100:
            processed = sharpen(processed)
            result.operations.append("Sharpen")
            result.is_blurry = True

        # Preserve edges
        processed = bilateral_filter(processed)
        result.operations.append("Bilateral Filter")

        # Resize
        processed = resize_image(processed)
        result.operations.append("Resize")

        # Normalize
        processed = normalize(processed)
        result.operations.append("Normalize")

        result.processed = processed

        return result