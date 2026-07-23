import cv2
import numpy as np


class ImageAnalyzer:

    def blur(self, gray):

        return cv2.Laplacian(
            gray,
            cv2.CV_64F
        ).var()

    def brightness(self, gray):

        return np.mean(gray)

    def contrast(self, gray):

        return np.std(gray)

    def noise(self, gray):

        smooth = cv2.GaussianBlur(
            gray,
            (3,3),
            0
        )

        return np.std(
            gray.astype(np.float32) -
            smooth.astype(np.float32)
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

        return np.mean(
            np.sqrt(gx**2 + gy**2)
        )

    def analyze(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        report = {}

        report["blur"] = self.blur(gray)

        report["brightness"] = self.brightness(gray)

        report["contrast"] = self.contrast(gray)

        report["noise"] = self.noise(gray)

        report["sharpness"] = self.sharpness(gray)

        return report