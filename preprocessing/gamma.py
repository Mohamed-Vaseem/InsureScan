import cv2
import numpy as np


def gamma_correction(image, gamma=1.25):
    """
    Applies mild gamma correction.

    Parameters
    ----------
    image : ndarray
        Input BGR image.

    gamma : float
        Gamma value (>1 brightens).

    Returns
    -------
    ndarray
        Corrected image.
    """

    inverse = 1.0 / gamma

    table = np.array(
        [
            ((i / 255.0) ** inverse) * 255
            for i in range(256)
        ],
        dtype=np.uint8
    )

    return cv2.LUT(image, table)