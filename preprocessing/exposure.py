import numpy as np


def exposure_score(gray):

    bright_pixels = np.sum(gray > 240)

    total_pixels = gray.size

    return (bright_pixels / total_pixels) * 100