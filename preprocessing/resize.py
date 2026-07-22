import cv2

def resize_image(image, width=640, height=640):
    """
    Resize image to the desired dimensions.

    Args:
        image: Input image
        width: Output width
        height: Output height

    Returns:
        Resized image
    """

    resized = cv2.resize(
        image,
        (width, height),
        interpolation=cv2.INTER_AREA
    )

    return resized