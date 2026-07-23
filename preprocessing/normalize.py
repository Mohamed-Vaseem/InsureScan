import cv2


def normalize(image):

    return cv2.normalize(
        image,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )