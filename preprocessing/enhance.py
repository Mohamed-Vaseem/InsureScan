import cv2

def enhance_image(image):
    """
    Enhance image contrast using CLAHE.

    Args:
        image: Input BGR image

    Returns:
        Contrast enhanced BGR image
    """

    # Convert BGR to LAB
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Split channels
    l, a, b = cv2.split(lab)

    # Create CLAHE object
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    # Apply CLAHE to Lightness channel
    l = clahe.apply(l)

    # Merge channels
    enhanced = cv2.merge((l, a, b))

    # Convert back to BGR
    enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)

    return enhanced