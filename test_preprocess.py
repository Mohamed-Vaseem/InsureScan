import cv2
from preprocessing.preprocess import preprocess

image = cv2.imread("assets/test.jpg")

if image is None:
    print("Image not found!")
    exit()

processed = preprocess(image)

cv2.imshow("Original", image)
cv2.imshow("Processed", processed)

cv2.imwrite("outputs/preprocessed.jpg", processed)

cv2.waitKey(0)
cv2.destroyAllWindows()