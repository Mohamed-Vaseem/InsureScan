import cv2

MODEL_SIZE = (640, 640)


def resize_image(image):

    return cv2.resize(
        image,
        MODEL_SIZE,
        interpolation=cv2.INTER_AREA
    )