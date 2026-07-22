import cv2

def remove_noise(image):
    """
    Remove image noise using Gaussian Blur.

    Args:
        image: Input image

    Returns:
        Denoised image
    """

    denoised = cv2.GaussianBlur(
        image,
        (5, 5),
        0
    )

    return denoised