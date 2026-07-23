import cv2


def remove_noise(image):

    return cv2.fastNlMeansDenoisingColored(
        image,
        None,
        7,
        7,
        7,
        21
    )