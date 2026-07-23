class ValidationResult:
    """
    Stores the validation results of an image.
    """

    def __init__(self):

        # -------------------------
        # Image Information
        # -------------------------

        self.width = 0
        self.height = 0
        self.channels = 0

        # -------------------------
        # Validation Flags
        # -------------------------

        self.is_valid = False

        self.is_corrupted = False

        self.too_small = False

        self.too_large = False

        # -------------------------
        # Messages
        # -------------------------

        self.warnings = []

        self.message = ""