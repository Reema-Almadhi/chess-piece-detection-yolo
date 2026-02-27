# YOLOv11 vs YOLOv12 for Chess Piece Detection

A comparison of the performance of YOLOv11 and YOLOv12 on a custom chess piece detection dataset, evaluated using precision, recall, mAP, and inference speed across 12 chess piece classes."

## Sample detection images

| YOLOv11 | YOLOv12 |
|---------|---------|
| <img src="https://github.com/user-attachments/assets/6b47602c-f98c-4159-afbb-26172484cd79" width="250"/> | <img src="https://github.com/user-attachments/assets/7ff3e053-4a79-42dd-ad9f-b3d63e3a4f45" width="250"/> |

## Dataset Details
- **Number of images:** 693  
- **Classes (12):** White/Black Pawn, Rook, Knight, Bishop, Queen, King  
- **Annotations:** YOLO format  
- **Data split:** Train / Validation / Test  
- **Preprocessing:** Roboflow  

## Training Settings
- **Image size:** 416×416  
- **Batch size:** 4  
- **Epochs:** 50  
- **Optimizer:** AdamW  
- **Learning rate:** 0.0002  

## Results

| Metric               | YOLOv11 | YOLOv12 |
|---------------------|---------|---------|
| Box Precision        | 96.9%   | 97%     |
| Recall               | 99%     | 97.9%   |
| mAP@0.5              | 98.9%   | 98.7%   |
| mAP@0.50:0.95        | 80.5%   | 81%     |
| Inference FPS        | 84.90   | 67.76   |
| Inference Time/Image | 9.4 ms  | 12.7 ms |

## Comparison Summary

Both models achieved over **98% mAP@0.5**.  
- YOLOv11 showed a 27% speed advantage with faster inference.  
- YOLOv12 achieved slightly higher mAP@0.50:0.95, suggesting marginally better localization precision.
