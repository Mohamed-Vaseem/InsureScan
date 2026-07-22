from PIL import Image


def load_image(path, size=(400, 300)):
    """
    Load and resize an image for display.

    Args:
        path: Image file path
        size: Desired display size

    Returns:
        PIL.Image object
    """

    image = Image.open(path)

    image.thumbnail(size)

    return image