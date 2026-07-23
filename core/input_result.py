class InputResult:
    """
    Stores everything produced during the
    image preparation stage.
    """

    def __init__(self):

        # Original image
        self.original = None

        # Vehicle crop
        self.cropped = None

        # Final image sent to YOLO
        self.processed = None

        # Validation report
        self.validation = None

        # Vehicle detection report
        self.vehicle = None

        # Preprocessing report
        self.preprocessing = None

        # Status
        self.success = False

        self.message = ""