from ultralytics import YOLO
import time
from pathlib import Path

MODEL_PATH = "runs/detect/train13/weights/best.pt"
TEST_IMAGES_DIR = "chess_pieces/test/images"
DATA_YAML = "data.yaml"  
BATCH_SIZE = 1

def evaluate():
    model = YOLO(MODEL_PATH)
    
    print("\n=== Model Info ===")
    model.info(verbose=True)  # layers, params, GFLOPs
    
    # Inference FPS
    test_images = list(Path(TEST_IMAGES_DIR).glob("*.*"))
    fps_list = []
    for img_path in test_images:
        start = time.time()
        results = model.predict(source=str(img_path), save=False, verbose=False)
        fps = 1 / (time.time() - start)
        fps_list.append(fps)
        print(f"{img_path.name} -> FPS: {fps:.2f}")
    print(f"\nAverage FPS: {sum(fps_list)/len(fps_list):.2f}")
    
    # Validation metrics
    print("\nRunning validation...")
    val_results = model.val(data=DATA_YAML, batch=BATCH_SIZE, verbose=True)
    print("Evaluation Complete")

if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()  # needed on Windows
    evaluate()
