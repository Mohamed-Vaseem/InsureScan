import cv2

from detection.damage_detector import DamageDetector

IMAGE_PATH = "test_images/car1.jpg"


def main():

    image = cv2.imread(IMAGE_PATH)

    if image is None:
        print("Failed to load image.")
        return

    detector = DamageDetector()

    result = detector.predict(image)

    print("=" * 50)
    print("Damage Detector")
    print("=" * 50)

    print("Success :", result.success)
    print("Message :", result.message)
    print("Count   :", result.count)

    if not result.success:
        return

    for i, damage in enumerate(result.detections, start=1):

        print(f"\nDamage #{i}")
        print("-" * 30)
        print(f"Class      : {damage.class_name}")
        print(f"Confidence : {damage.confidence:.3f}")
        print(f"Area       : {damage.area}")
        print(f"Box        : {damage.bounding_box}")

        if damage.polygon is not None:
            print(f"Polygon points : {len(damage.polygon)}")

    cv2.imshow("Damage Detection", result.annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()