class PreprocessingResult:

    def __init__(self):

        # Images
        self.original = None
        self.processed = None

        # Measurements
        self.blur_score = 0
        self.noise_score = 0
        self.brightness = 0
        self.contrast = 0
        self.sharpness = 0

        # Flags
        self.is_blurry = False
        self.is_noisy = False
        self.is_dark = False
        self.low_contrast = False

        # Quality
        self.quality_score = 0

        # Processing
        self.operations = []

        # Messages
        self.warnings = []