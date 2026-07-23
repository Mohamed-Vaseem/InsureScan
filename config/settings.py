"""
Global configuration for InsureScan.

All configurable values should be stored here instead of hardcoding
them inside the project.
"""


class Settings:

    # ==========================
    # Image Validation
    # ==========================

    MIN_WIDTH = 640
    MIN_HEIGHT = 480

    MAX_WIDTH = 6000
    MAX_HEIGHT = 6000

    # ==========================
    # Image Analysis Thresholds
    # ==========================

    MIN_BRIGHTNESS = 80
    MIN_CONTRAST = 40

    MAX_NOISE = 20

    MIN_BLUR_SCORE = 100

    # ==========================
    # Vehicle Crop
    # ==========================

    CROP_MARGIN = 0.10      # 10%

    # ==========================
    # Preprocessing
    # ==========================

    RESIZE_WIDTH = 640
    RESIZE_HEIGHT = 640

    # ==========================
    # YOLO
    # ==========================

    CONFIDENCE_THRESHOLD = 0.30

    IOU_THRESHOLD = 0.45

    # ==========================
    # Logging
    # ==========================

    ENABLE_LOGS = True