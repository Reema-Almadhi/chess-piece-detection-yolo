from ultralytics import YOLO

if __name__ == "__main__":
    # Load YOLOv11 small model
    model = YOLO("yolo11s.pt")
    
    # Train on chess dataset
    model.train(
        data="data.yaml",   # dataset config
        epochs=50,
        imgsz=416,
        batch=16,
        device="0"          # GPU 0
    )
