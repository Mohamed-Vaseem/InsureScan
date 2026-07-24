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

        # Damage segmentation image
        self.segmented = None

        # Part segmentation image
        self.part_segmented = None

        # =============================
        # Pipeline Results
        # =============================

        self.input = None

        self.damage = None

        self.part = None

        # =============================
        # Metadata
        # =============================

        self.processing_time = 0.0

        self.success = False

        self.message = ""