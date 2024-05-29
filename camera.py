import cv2
import yaml

with open('config/settings.yaml', 'r') as file:
    config = yaml.safe_load(file)

def capture_frame():
    cap = cv2.VideoCapture(config['camera']['path'])
    
    if not cap.isOpened():
        print("Error: Could not open video capture")
        return None
    
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        print("Error: Could not read frame")
        return None
    
    return frame
