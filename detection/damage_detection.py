import numpy as np


class DamageDetection:
    """
    Represents a single detected damage instance.
    """

    def __init__(self):

        self.class_id = -1

        self.class_name = ""

        self.confidence = 0.0

        self.bounding_box = None

        self.mask = None

        self.polygon = None

        self.area = 0

    @property
    def has_mask(self):

        return self.mask is not None