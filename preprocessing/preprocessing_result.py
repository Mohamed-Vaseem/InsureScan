from preprocessing.analysis_result import AnalysisResult


class PreprocessingResult:
    """
    Stores the output of the preprocessing stage.
    """

    def __init__(self):

        # Original input
        self.original = None

        # Final processed image
        self.processed = None

        # Image analysis
        self.analysis = AnalysisResult()

        # Status
        self.success = False

        self.message = ""