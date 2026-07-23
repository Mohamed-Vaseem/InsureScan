import cv2

from config import Settings


def resize_image(image):
    """
    Resize image to the network input size.
    """

    return cv2.resize(
        image,
        (
            Settings.RESIZE_WIDTH,
            Settings.RESIZE_HEIGHT
        ),
        interpolation=cv2.INTER_AREA
    )