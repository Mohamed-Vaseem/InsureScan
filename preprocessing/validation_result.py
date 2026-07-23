class ValidationResult:
    """
    Stores image validation results.

    This class is intentionally independent from preprocessing
    because validation happens before any enhancement.
    """

    def __init__(self):

        self.is_valid = True

        self.width = 0
        self.height = 0

        self.channels = 0

        self.orientation = "Unknown"

        self.is_corrupted = False

        self.too_small = False
        self.too_large = False

        self.warnings = []