# Import Libraries
import cv2
import torch

cap = cv2.VideoCapture(0)

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=True)
# Insert Yolov5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights\weight_v2.pt')

model = torch.hub.load('yolov5', 'custom', path="weights\weight_v2.pt", source='local')

while 1:
    ret,img = cap.read()
        
    cv2.imshow('img', img)
    results = model(img)
    print('Here are your results loop ', results)
    results.print()

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()