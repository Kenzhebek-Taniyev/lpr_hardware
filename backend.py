import requests
import cv2
import numpy as np
import yaml 

with open('config/settings.yaml', 'r') as file:
    config = yaml.safe_load(file)

def send_frame_to_backend(frame):
    url = config['api_settings']['base_url']
    _, img_encoded = cv2.imencode('.jpg', frame)
    files = {'file': ('image.jpg', img_encoded.tobytes(), 'image/jpeg')}
    
    return {'action': 'open'}

    # try:
    #     response = requests.post(url, files=files)
    #     response.raise_for_status()
    #     return response.json()
    # except requests.RequestException as e:
    #     print(f"Error: {e}")
    #     return {'action': 'close'}
