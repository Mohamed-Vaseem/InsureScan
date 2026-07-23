class InputResult:
    """
    Result returned by InputManager.
    """

    def __init__(self):

        # Images
        self.original = None
        self.cropped = None
        self.processed = None

        # Results
        self.validation = None
        self.vehicle = None
        self.preprocessing = None

        # Status
        self.success = False
        self.message = ""