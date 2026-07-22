from preprocessing.resize import resize_image
from preprocessing.denoise import remove_noise


def preprocess(image):
    """
    Image preprocessing pipeline.

    Steps:
        1. Resize image
        2. Light noise reduction

    Args:
        image: Input BGR image

    Returns:
        Preprocessed image
    """

    image = resize_image(image)

    image = remove_noise(image)

    return image