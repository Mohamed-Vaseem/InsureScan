class VehicleResult:
    """
    Stores the vehicle detection result.
    """

    def __init__(self):

        self.found = False

        self.confidence = 0.0

        self.bounding_box = None

        self.class_name = ""

        self.cropped_image = None

        self.margin = 0.0

        self.processing_time = 0.0