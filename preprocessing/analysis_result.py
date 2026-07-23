class AnalysisResult:
    """
    Stores image quality analysis results.
    """

    def __init__(self):

        self.blur = 0.0
        self.brightness = 0.0
        self.contrast = 0.0
        self.noise = 0.0
        self.sharpness = 0.0

        self.recommendations = []