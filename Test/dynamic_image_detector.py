# Import Libraries
import cv2
import torch

# Assigns local webcam to cap variable
cap = cv2.VideoCapture(0)

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=True)
# Insert Yolov5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights\weight_v2.pt', force_reload=True)

model = torch.hub.load('yolov5', 'custom', path="weights\weight_v2.pt", source='local')

while 1:
    ret,img = cap.read()

    # Running inference on detected images with current weights
    results = model(img)
    # Takes original img and updates it with bounding boxes and labels
    results.render()

    # Creates display screen showing livestreaming of images detected
    cv2.imshow('Output', img)
    # Prints the results of inference (detected items) to the terminal
    results.print()

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()