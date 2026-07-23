import cv2


class Cropper:

    """
    Generic crop utility.

    Can crop any object given
    a bounding box.
    """

    @staticmethod
    def crop(image, bbox, margin=0.10):

        x1, y1, x2, y2 = bbox

        h, w = image.shape[:2]

        bw = x2 - x1
        bh = y2 - y1

        mx = int(bw * margin)
        my = int(bh * margin)

        x1 = max(0, x1 - mx)
        y1 = max(0, y1 - my)

        x2 = min(w, x2 + mx)
        y2 = min(h, y2 + my)

        return image[y1:y2, x1:x2]