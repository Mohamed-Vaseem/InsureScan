from ultralytics import YOLO
import numpy as np
import cv2


class DamagePartAnalyzer:

    def __init__(self, part_model_path, damage_model_path):
        self.part_model = YOLO(part_model_path)
        self.damage_model = YOLO(damage_model_path)

    def mask_iou(self, mask1, mask2):
        intersection = np.logical_and(mask1, mask2).sum()
        union = np.logical_or(mask1, mask2).sum()

        if union == 0:
            return 0

        return intersection / union

    def analyze(self, image_path):

        part_result = self.part_model.predict(
            image_path,
            conf=0.25,
            verbose=False
        )[0]

        damage_result = self.damage_model.predict(
            image_path,
            conf=0.25,
            verbose=False
        )[0]

        results = []

        # No detections
        if part_result.masks is None or damage_result.masks is None:
            return results

        part_masks = part_result.masks.data.cpu().numpy()
        damage_masks = damage_result.masks.data.cpu().numpy()

        part_boxes = part_result.boxes
        damage_boxes = damage_result.boxes

        for d_index, d_mask in enumerate(damage_masks):

            best_iou = 0
            best_part = None

            for p_index, p_mask in enumerate(part_masks):

                iou = self.mask_iou(d_mask > 0.5, p_mask > 0.5)

                if iou > best_iou:
                    best_iou = iou
                    best_part = p_index

            if best_part is not None:

                damage_class = int(damage_boxes.cls[d_index])
                damage_name = damage_result.names[damage_class]

                part_class = int(part_boxes.cls[best_part])
                part_name = part_result.names[part_class]

                confidence = float(damage_boxes.conf[d_index])

                results.append({
                    "part": part_name,
                    "damage": damage_name,
                    "confidence": round(confidence, 2),
                    "iou": round(best_iou, 3)
                })

        return results