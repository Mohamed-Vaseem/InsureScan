class Settings:
    """
    Global configuration for InsureScan.
    All project-wide settings should be placed here.
    """

    # ==========================================
    # Image Validation
    # ==========================================

    MIN_WIDTH = 640
    MIN_HEIGHT = 480

    MAX_WIDTH = 6000
    MAX_HEIGHT = 6000

    # ==========================================
    # Image Analysis
    # ==========================================

    MIN_BRIGHTNESS = 80
    MIN_CONTRAST = 40

    # Variance of Laplacian
    MIN_BLUR_SCORE = 100

    # Estimated image noise
    MAX_NOISE = 40

    # ==========================================
    # Vehicle Detection
    # ==========================================

    VEHICLE_MODEL = "models/vehicle/yolo11n.pt"

    VEHICLE_CONFIDENCE = 0.35
    VEHICLE_IOU = 0.45

    CROP_MARGIN = 20

    # ==========================================
    # Damage Detection
    # ==========================================

    DAMAGE_MODEL = "models/damage/best.pt"

    DAMAGE_CONFIDENCE = 0.25
    DAMAGE_IOU = 0.45

    # ==========================================
    # Image Processing
    # ==========================================

    RESIZE_WIDTH = 1024
    RESIZE_HEIGHT = 768

    # ==========================================
    # Logging
    # ==========================================

    ENABLE_LOGS = True