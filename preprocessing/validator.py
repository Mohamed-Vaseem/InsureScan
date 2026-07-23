import cv2

from config import Settings

from preprocessing.validation_result import ValidationResult


class ImageValidator:
    """
    Validates an image before entering
    the AI pipeline.
    """

    def validate(self, image):

        result = ValidationResult()

        # -------------------------
        # Image Exists
        # -------------------------

        if image is None:

            result.is_corrupted = True

            result.message = "Image is empty."

            return result

        # -------------------------
        # Image Size
        # -------------------------

        height, width = image.shape[:2]

        result.width = width

        result.height = height

        result.channels = image.shape[2]

        # -------------------------
        # Minimum Size
        # -------------------------

        if width < Settings.MIN_WIDTH:

            result.too_small = True

            result.warnings.append(
                "Image width is too small."
            )

        if height < Settings.MIN_HEIGHT:

            result.too_small = True

            result.warnings.append(
                "Image height is too small."
            )

        # -------------------------
        # Maximum Size
        # -------------------------

        if width > Settings.MAX_WIDTH:

            result.too_large = True

            result.warnings.append(
                "Image width exceeds limit."
            )

        if height > Settings.MAX_HEIGHT:

            result.too_large = True

            result.warnings.append(
                "Image height exceeds limit."
            )

        # -------------------------
        # Final Decision
        # -------------------------

        if result.too_small:

            result.message = "Image resolution is too low."

            return result

        if result.too_large:

            result.message = "Image resolution is too high."

            return result

        result.is_valid = True

        result.message = "Validation successful."

        return result