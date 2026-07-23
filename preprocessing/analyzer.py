import cv2
import numpy as np

from config import Settings

from preprocessing.analysis_result import AnalysisResult


class ImageAnalyzer:
    """
    Analyses image quality.

    This class NEVER modifies an image.
    It only measures image quality and
    recommends preprocessing steps.
    """

    def __init__(self):
        pass

    # -------------------------------------------------
    # Brightness
    # -------------------------------------------------

    def calculate_brightness(self, gray):

        return float(np.mean(gray))

    # -------------------------------------------------
    # Contrast
    # -------------------------------------------------

    def calculate_contrast(self, gray):

        return float(np.std(gray))

    # -------------------------------------------------
    # Blur
    # -------------------------------------------------

    def calculate_blur(self, gray):

        return float(
            cv2.Laplacian(
                gray,
                cv2.CV_64F
            ).var()
        )

    # -------------------------------------------------
    # Noise
    # -------------------------------------------------

    def calculate_noise(self, gray):

        smooth = cv2.GaussianBlur(
            gray,
            (3, 3),
            0
        )

        noise = gray.astype(np.float32) - smooth.astype(np.float32)

        return float(
            np.std(noise)
        )

    # -------------------------------------------------
    # Sharpness
    # -------------------------------------------------

    def calculate_sharpness(self, gray):

        gx = cv2.Sobel(
            gray,
            cv2.CV_64F,
            1,
            0
        )

        gy = cv2.Sobel(
            gray,
            cv2.CV_64F,
            0,
            1
        )

        magnitude = np.sqrt(
            gx ** 2 +
            gy ** 2
        )

        return float(
            np.mean(magnitude)
        )

    # -------------------------------------------------
    # Main Analysis
    # -------------------------------------------------

    def analyze(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        result = AnalysisResult()

        result.brightness = self.calculate_brightness(gray)

        result.contrast = self.calculate_contrast(gray)

        result.blur = self.calculate_blur(gray)

        result.noise = self.calculate_noise(gray)

        result.sharpness = self.calculate_sharpness(gray)

        # ---------------------------------------------
        # Recommendations
        # ---------------------------------------------

        if result.brightness < Settings.MIN_BRIGHTNESS:

            result.need_gamma = True

            result.recommendations.append(
                "Apply Gamma Correction"
            )

        if result.contrast < Settings.MIN_CONTRAST:

            result.need_clahe = True

            result.recommendations.append(
                "Apply CLAHE"
            )

        height, width = image.shape[:2]

        if (
            width != Settings.RESIZE_WIDTH or
            height != Settings.RESIZE_HEIGHT
        ):

            result.need_resize = True

            result.recommendations.append(
                "Resize Image"
            )

        return result