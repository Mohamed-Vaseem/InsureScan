import cv2
from preprocessing.enhance import enhance_image

image = cv2.imread("assets/test.jpg")

if image is None:
    print("Image not found!")
    exit()

enhanced = enhance_image(image)

cv2.imshow("Original", image)
cv2.imshow("Enhanced", enhanced)

cv2.imwrite("outputs/enhanced.jpg", enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()