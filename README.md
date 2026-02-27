# YOLOv11 vs YOLOv12 for Chess Piece Detection

A comparison of the performance of YOLOv11 and YOLOv12 on a custom chess piece detection dataset, evaluated using accuracy, speed, and generalization across 12 chess piece classes.

Sample detection images:
YOLOv11:

 ![f1a24b6bb778ee11ba33687415aa84f2_jpg rf f2646d2d46b39f6510975f24d554bae1](https://github.com/user-attachments/assets/6b47602c-f98c-4159-afbb-26172484cd79)

YOLOv12:

 ![b9402881fa580d0eb8b9b98845417550_jpg rf 7c401587706c0c03dab27877a8d22f55](https://github.com/user-attachments/assets/7ff3e053-4a79-42dd-ad9f-b3d63e3a4f45)

Dataset details:
- 693 images.
- 12 classes: White/Black Pawn, Rook, Knight, Bishop, Queen, King.
- Annotated in YOLO format.
- Train/Validation/Test split.
- Preprocessed using Roboflow.

Training Settings:
- Image size: 416x416
- Batch size: 4
- Epochs: 50
- Optimizer: AdamW
- Learning rate: 0.0002

Results:
- YOLOv11:
- box precision: 96.9%
- recall: 99%
- mAP@0.5: 98.9%
- mAP@0.50:0.95: 80.5%
- Inference FPS: 84.90
- Inference Time/Image: 9.4 ms
  
- YOLOv12:
- box precision: 97%
- recall: 97.9%
- mAP@0.5: 98.7%
- mAP@0.50:0.95: 81%
- Inference FPS: 67.76
- Inference Time/Image: 12.7 ms

Results summary:
Both models achieved over 98% accuracy in mAP@0.5.
YOLOv11 displayed a 27% speed advantage with faster inference time.
YOLOv12 demonstrated better generalization in complex scenarios.
