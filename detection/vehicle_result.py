class VehicleResult:
    """
    Stores the result of vehicle detection.
    """

    def __init__(self):

        # Status
        self.success = False
        self.detected = False
        self.message = ""

        # Detection
        self.class_name = ""
        self.confidence = 0.0
        self.bounding_box = None

        # Images
        self.cropped_image = None
        self.annotated_image = None