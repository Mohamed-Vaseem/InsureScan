import cv2
import numpy as np

from preprocessing.analysis_result import AnalysisResult


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
                gray.astype(np.float32) -
                smooth.astype(np.float32)
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

        result = AnalysisResult()

        result.blur = self.blur(gray)
        result.brightness = self.brightness(gray)
        result.contrast = self.contrast(gray)
        result.noise = self.noise(gray)
        result.sharpness = self.sharpness(gray)

        if result.brightness < 80:
            result.recommendations.append(
                "Increase Brightness"
            )

        if result.contrast < 40:
            result.recommendations.append(
                "Improve Contrast"
            )

        return result