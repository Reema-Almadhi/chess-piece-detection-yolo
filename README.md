# YOLO11 vs YOLO12 for Chess Piece Detection

Description:
a comparison of two chess piece detection models using YOLO11 and YOLO12 models.

Dataset:
-693 images.
-12 classes: White/Black Pawn, Rook, Knight, Bishop, Queen, King.
-Annotated in YOLO format.
-Train/Validation/Test split.
-Preprocessed using Roboflow.


Training Settings:
-Image size: 416x416
-Batch size: 4
-Epochs: 50
-Optimizer: adamW
-learning rate: 0.0002


-Evaluation Metrics:
- Precision
- Recall
- mAP@0.50
-mAP@0.50:0.95
-Inference FPS
-Inference Time/Image

Results:
-YOLOv12:
box precision: 97%
recall: 97.9%
mAP@0.5: 98.7%

-YOLOv11:
box precision: 96.9%
recall: 99%
mAP@0.5: 98.9%
