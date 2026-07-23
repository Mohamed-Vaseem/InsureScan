import cv2

from config import Settings

from preprocessing.validation_result import ValidationResult


class ImageValidator:

    """
    Performs basic validation before the image
    enters the preprocessing pipeline.
    """

    def validate(self, image):

        result = ValidationResult()

        # -------------------------
        # Image Exists
        # -------------------------

        if image is None:

            result.is_valid = False
            result.is_corrupted = True
            result.warnings.append("Image could not be loaded.")

            return result

        # -------------------------
        # Dimensions
        # -------------------------

        h, w = image.shape[:2]

        result.width = w
        result.height = h

        if len(image.shape) == 3:
            result.channels = image.shape[2]
        else:
            result.channels = 1

        # -------------------------
        # Orientation
        # -------------------------

        if w > h:
            result.orientation = "Landscape"

        elif h > w:
            result.orientation = "Portrait"

        else:
            result.orientation = "Square"

        # -------------------------
        # Resolution Checks
        # -------------------------

        if w < Settings.MIN_WIDTH or h < Settings.MIN_HEIGHT:

            result.too_small = True

            result.warnings.append(
                "Image resolution is too low."
            )

        if w > Settings.MAX_WIDTH or h > Settings.MAX_HEIGHT:

            result.too_large = True

            result.warnings.append(
                "Image resolution is very high."
            )

        # -------------------------
        # Final Decision
        # -------------------------

        if result.too_small:

            result.is_valid = False

        return result