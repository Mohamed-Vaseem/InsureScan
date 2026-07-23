import numpy as np


def normalize_image(image):
    """
    Normalize image to float32 [0,1].

    This is intended for deep learning models.
    """

    image = image.astype(np.float32)

    image /= 255.0

    return image