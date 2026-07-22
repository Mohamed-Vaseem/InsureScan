import cv2
from preprocessing.resize import resize_image

image = cv2.imread("assets/test.jpg")

if image is None:
    print("Image not found!")
    exit()

resized = resize_image(image)

cv2.imshow("Original", image)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()