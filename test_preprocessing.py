import cv2

from core.image_manager import ImageManager
from core.input_manager import InputManager


def main():

    image_path = "test_images/car.jpg"   # Change to your test image

    manager = ImageManager()
    image = manager.load(image_path)

    pipeline = InputManager()

    result = pipeline.prepare(image)

    print("\n========== INPUT MANAGER ==========")
    print(f"Success : {result.success}")
    print(f"Message : {result.message}")

    if result.validation:
        print("\nValidation")
        print(f"Valid   : {result.validation.is_valid}")
        print(f"Size    : {result.validation.width} x {result.validation.height}")

    if result.vehicle:
        print("\nVehicle Detection")
        print(result.vehicle)

    if result.preprocessing:
        print("\nImage Analysis")
        print(f"Brightness : {result.preprocessing.analysis.brightness:.2f}")
        print(f"Contrast   : {result.preprocessing.analysis.contrast:.2f}")
        print(f"Blur       : {result.preprocessing.analysis.blur:.2f}")
        print(f"Noise      : {result.preprocessing.analysis.noise:.2f}")
        print(f"Sharpness  : {result.preprocessing.analysis.sharpness:.2f}")

    if result.processed is not None:

        cv2.imshow("Processed", result.processed)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()