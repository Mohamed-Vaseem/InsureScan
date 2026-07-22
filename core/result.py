class ProcessingResult:
    """
    Stores everything produced during the AI pipeline.
    """

    def __init__(self):

        # Images
        self.original = None
        self.preprocessed = None
        self.detected = None

        # Detection Information
        self.damage_type = None
        self.confidence = None
        self.severity = None

        # Performance
        self.processing_time = None

        # Status
        self.success = False
        self.message = ""