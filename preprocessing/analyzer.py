import cv2
import numpy as np

from preprocessing.config import (
    BLUR_MEDIUM,
    BRIGHTNESS_LOW,
    BRIGHTNESS_HIGH,
    CONTRAST_THRESHOLD,
    NOISE_THRESHOLD
)

from preprocessing.exposure import exposure_score


class ImageAnalyzer:

    def blur(self, gray):

        return cv2.Laplacian(
            gray,
            cv2.CV_64F
        ).var()

    def brightness(self, gray):

        return float(np.mean(gray))

    def contrast(self, gray):

        return float(np.std(gray))

    def noise(self, gray):

        smooth = cv2.GaussianBlur(
            gray,
            (3, 3),
            0
        )

        return float(
            np.std(
                gray.astype(np.float32)
                - smooth.astype(np.float32)
            )
        )

    def sharpness(self, gray):

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

        return float(
            np.mean(
                np.sqrt(gx ** 2 + gy ** 2)
            )
        )

    def analyze(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        height, width = gray.shape

        report = {}

        report["blur"] = self.blur(gray)
        report["brightness"] = self.brightness(gray)
        report["contrast"] = self.contrast(gray)
        report["noise"] = self.noise(gray)
        report["sharpness"] = self.sharpness(gray)

        report["width"] = width
        report["height"] = height

        report["overexposure"] = exposure_score(gray)

        report["is_blurry"] = report["blur"] < BLUR_MEDIUM
        report["is_dark"] = report["brightness"] < BRIGHTNESS_LOW
        report["is_bright"] = report["brightness"] > BRIGHTNESS_HIGH
        report["low_contrast"] = report["contrast"] < CONTRAST_THRESHOLD
        report["is_noisy"] = report["noise"] > NOISE_THRESHOLD

        return report