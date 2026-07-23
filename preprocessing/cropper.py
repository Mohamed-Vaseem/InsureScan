from config import Settings


class VehicleCropper:
    """
    Crops the detected vehicle from the image.
    """

    def crop(self, image, box):

        """
        Parameters
        ----------
        image : ndarray

        box : (x1, y1, x2, y2)

        Returns
        -------
        Cropped vehicle image.
        """

        x1, y1, x2, y2 = map(int, box)

        margin = Settings.CROP_MARGIN

        x1 = max(0, x1 - margin)
        y1 = max(0, y1 - margin)

        x2 = min(image.shape[1], x2 + margin)
        y2 = min(image.shape[0], y2 + margin)

        return image[y1:y2, x1:x2].copy()