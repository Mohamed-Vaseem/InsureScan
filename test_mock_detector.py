import cv2

from detection.damage_detector import DamageDetector

image = cv2.imread("test_images/car1.jpg")

detector = DamageDetector()

result = detector.predict(image)

print("Success :", result.success)
print("Message :", result.message)
print("Count   :", result.count)

for damage in result.detections:
    print("Class      :", damage.class_name)
    print("Confidence :", damage.confidence)

cv2.imshow("Mock Detection", result.annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()