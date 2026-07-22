import cv2


class ImageManager:

    def __init__(self):

        self.image_path = None

        self.original = None

        self.preprocessed = None

        self.result = None

    def load(self, path):

        self.image_path = path

        self.original = cv2.imread(path)

        return self.original