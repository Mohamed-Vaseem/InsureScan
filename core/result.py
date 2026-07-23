class ProcessingResult:
    """
    Stores everything produced by the
    complete InsureScan pipeline.
    """

    def __init__(self):

        # -------------------------
        # Input Stage
        # -------------------------

        self.input = None

        # -------------------------
        # Detection Stage
        # -------------------------

        self.damage = None

        # -------------------------
        # Output Images
        # -------------------------

        self.original = None

        self.cropped = None

        self.preprocessed = None

        self.detected = None

        # -------------------------
        # AI Results
        # -------------------------

        self.damage_type = None

        self.confidence = None

        self.severity = None

        # -------------------------
        # Performance
        # -------------------------

        self.processing_time = 0.0

        # -------------------------
        # Status
        # -------------------------

        self.success = False

        self.message = ""