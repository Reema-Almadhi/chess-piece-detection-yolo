from ultralytics import YOLO
from pathlib import Path
import shutil

model = YOLO("runs/detect/train13/weights/best.pt")

test_folder = Path("chess_pieces/test/images")
save_folder = Path("test_results/annotated")
save_folder.mkdir(parents=True, exist_ok=True)

for img_path in test_folder.glob("*.*"):
    results = model(str(img_path))
    for r in results:
        # Copy annotated image to our folder
        annotated_image = Path("predict") / Path(r.path).name  # default YOLO save folder
        shutil.copy(annotated_image, save_folder)
