import cv2
from preprocessing.edge import enhance_edges

image = cv2.imread("assets/test.jpg")

if image is None:
    print("Image not found!")
    exit()

edged = enhance_edges(image)

cv2.imshow("Original", image)
cv2.imshow("Sharpened", edged)

cv2.imwrite("outputs/sharpened.jpg", edged)

cv2.waitKey(0)
cv2.destroyAllWindows()