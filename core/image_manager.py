import cv2
import os


class ImageManager:
    """
    Handles loading and saving images.
    """

    def __init__(self):

        self.image_path = None

    def load(self, path):

        if not os.path.exists(path):
            raise FileNotFoundError(path)

        image = cv2.imread(path)

        if image is None:
            raise ValueError("Unable to read image.")

        self.image_path = path

        return image

    def save(self, path, image):

        cv2.imwrite(path, image)