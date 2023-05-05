# Import Libraries
import os
import cv2
import torch


from intrinsic_extrinsic import slamLogicHandler
current_directory = os.path.dirname(os.path.abspath(__file__))
coordinateConverter = slamLogicHandler()

# Assigns local webcam to cap variable
cap = cv2.VideoCapture(0)

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=True)
# Insert Yolov5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/weight_v3.pt', force_reload=True)

model = torch.hub.load('yolov5', 'custom', path="weights/weight_v3.pt", source='local')

while 1:
    ret,img = cap.read()

    # Running inference on detected images with current weights
    results = model(img)
    # Takes original img and updates it with bounding boxes and labels
    results.render()

    # Creates display screen showing livestreaming of images detected
    cv2.imshow('Output', img)
    # Prints the results of inference (detected items) to the terminal
    # results.print()
    x_min = results.pandas().xyxy[0]['xmin']
    y_min = results.pandas().xyxy[0]['ymin']
    x_max = results.pandas().xyxy[0]['xmax']
    y_max = results.pandas().xyxy[0]['ymax']

    if x_min.empty is False:
        # Normallizing the above values -> Giving them as a porition fo the whole image
        x = x_min[0]/x_max[0]
        y = y_min[0]/y_max[0]
        # width = int((x_max[0] - x_min[0]) / x_max[0])
        # height = int((y_max[0] - y_min[0]) / y_max[0])

        # Depth will be an entire equation: Based on position of camera's starting point.
        # We will approximate the depth by gathering the values of x and y at the corner point of the testing area and use that as a sampling point
        intrinsic_depth = 100 # This is for now

        params = {
            'intr_x': x,
            'intr_y': y,
            'depth': intrinsic_depth
        }
        # print(params)
        ext_param_x, ext_params_y, ext_param_z = coordinateConverter.intrinsicParamConvert(params, excelSave=False)
        # print('x= ' + str(ext_param_x) + ' y= ' + str(ext_params_y) + ' z= ' + str(ext_param_z))
        print('Converted coordinates to their world coordinates')

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()