from preprocessing.config import (
    BLUR_MEDIUM,
    NOISE_THRESHOLD,
    BRIGHTNESS_LOW,
    CONTRAST_THRESHOLD
)


def calculate_quality(report):

    score = 100

    if report["blur"] < BLUR_MEDIUM:
        score -= 15

    if report["noise"] > NOISE_THRESHOLD:
        score -= 10

    if report["brightness"] < BRIGHTNESS_LOW:
        score -= 10

    if report["contrast"] < CONTRAST_THRESHOLD:
        score -= 10

    if report["overexposure"] > 15:
        score -= 10

    return max(score, 0)