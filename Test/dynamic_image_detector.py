# Importing Libraries
import cv2
import os
import torch
from PIL import Image
import io
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
    # Reading in frames from camera
    success, img = cap.read()
    # Converting each frame to gray scale
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Import in the Yolo model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights\weight_v2.pt', force_reload=True) # Load local model weights
    model = torch.hub.load('yolov5', 'custom', path="weights\weight_v2.pt", source='local', force_reload=True) # Load Local yolov repo
    
    # This is where the custom code begins.
    if success == True:
        ret,buff = cv2.imencode('.jpg', img)
        img = buff.tobytes()
        
        frame = Image.open(io.BytesIO(img))
        results = model(frame)
        results.print()
        
        frame = np.squeeze(results.render())
        img_BGR = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    else:
        break
    
    # cv2.imshow('img', img)
    frame = cv2.imencode('.jpg', img_BGR)[1].tobytes()