from ai.damage_part_analyzer import DamagePartAnalyzer

analyzer = DamagePartAnalyzer(
    part_model_path=r"C:\Users\Vaseem\runs\segment\training\part_segmentation\weights\best.pt",
    damage_model_path=r"C:\Users\Vaseem\runs\segment\training\damage_segmentation\weights\best.pt"
)

results = analyzer.analyze("test.jpg")

print("\nDetected Results\n")

for item in results:
    print(
        f"{item['part']}  -->  {item['damage']} "
        f"(Confidence: {item['confidence']}, IoU: {item['iou']})"
    )