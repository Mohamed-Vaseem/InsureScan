import cv2

def remove_noise(image, kernel_size=3):
    """
    Apply a light Gaussian blur.
    """

    return cv2.GaussianBlur(
        image,
        (kernel_size, kernel_size),
        0
    )   