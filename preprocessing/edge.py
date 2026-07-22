import cv2
import numpy as np

def enhance_edges(image):
    """
    Sharpen the image using a sharpening kernel.
    This improves edge definition while preserving the original image.
    """

    kernel = np.array([
        [ 0, -1,  0],
        [-1,  5, -1],
        [ 0, -1,  0]
    ])

    sharpened = cv2.filter2D(image, -1, kernel)

    return sharpened