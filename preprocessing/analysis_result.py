class AnalysisResult:
    """
    Stores image quality measurements.
    """

    def __init__(self):

        # -------------------------
        # Image Statistics
        # -------------------------

        self.brightness = 0.0

        self.contrast = 0.0

        self.blur = 0.0

        self.noise = 0.0

        self.sharpness = 0.0

        # -------------------------
        # Recommendations
        # -------------------------

        self.need_gamma = False

        self.need_clahe = False

        self.need_resize = False

        # -------------------------
        # Messages
        # -------------------------

        self.recommendations = []