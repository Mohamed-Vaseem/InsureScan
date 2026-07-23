class ProcessingResult:
    """
    Final pipeline output.
    """

    def __init__(self):

        # =============================
        # Images
        # =============================

        self.original = None

        self.cropped = None

        self.preprocessed = None

        self.segmented = None

        # =============================
        # Pipeline Results
        # =============================

        self.input = None

        self.damage = None

        # =============================
        # Metadata
        # =============================

        self.processing_time = 0.0

        self.success = False

        self.message = ""