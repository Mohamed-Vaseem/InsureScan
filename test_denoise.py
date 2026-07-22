import cv2
from preprocessing.denoise import remove_noise

image = cv2.imread("assets/test.jpg")

if image is None:
    print("Error: Could not load image.")
    exit()

denoised = remove_noise(image)

cv2.imshow("Original", image)
cv2.imshow("Denoised", denoised)

cv2.imwrite("outputs/denoised.jpg", denoised)

cv2.waitKey(0)
cv2.destroyAllWindows()