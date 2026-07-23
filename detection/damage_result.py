from detection.damage_detection import DamageDetection


class DamageResult:
    """
    Stores the complete output of the
    damage segmentation model.
    """

    def __init__(self):

        self.success = False

        self.message = ""

        self.annotated_image = None

        self.detections: list[DamageDetection] = []

    @property
    def count(self):

        return len(self.detections)