# Import Libraries
import os
import cv2
import torch
import numpy as np


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
        x = float(x_min[0]/x_max[0])
        x = round(x,2)
        y = float(y_min[0]/y_max[0])
        y = round(y,2)
        # width = int((x_max[0] - x_min[0]) / x_max[0])
        # height = int((y_max[0] - y_min[0]) / y_max[0])
        """
            Depth will be an entire equation: Based on position of camera's starting point.
            We will approximate the depth by gathering the values of x and y at the corner point of the testing area and use that as a sampling point

            Question to think about within the lab: Does the depth change going straight up vs. side to side
            - My current hypothesis is that if I measure the depth at the midpoint on one side, the depth at the midpoint on the other side should be approx. the same. And same could be hypothesized for the middle point as well.
            - Which makes me think that with all this information and measured data we can pretty much be able to calculate the depth at any point within the frame as long as we have these 5 depth points

            Future Question to Consider: Could the below logic be simplified?
        """
        print('This is your x value: ', x)
        print('This is your y value: ', y)

        x_first = [0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.80]
        y_first = [0.77, 0.78, 0.79, 0.80, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86]

        x_two = [0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90, 0.91]
        y_two = [0.82, 0.83, 0.84, 0.85, 0.86, 0.87]

        x_third = [0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90]
        y_third = [0.80, 0.81, 0.82, 0.83, 0.84, 0.85]

        x_four = [0.89, 0.90, 0.91, 0.92, 0.93, 0.94]
        y_four = [0.78, 0.79, 0.80, 0.81, 0.82, 0.83, 0.84, 0.85]

        # Updated Calculation Metric
        if x in x_first and y in y_first:
            print('I am going inside of the first if statement')
            intrinsic_depth = 96 # This is in inches
            params = {
                'intr_x': x,
                'intr_y': y,
                'depth': intrinsic_depth
            }
            ext_param_x, ext_params_y, ext_param_z = coordinateConverter.intrinsicParamConvert(params)
        elif x in x_two and y in y_two:
            print('I am running within the first elif statement ')
            intrinsic_depth = 141 # This is in inches
            params = {
                'intr_x': x,
                'intr_y': y,
                'depth': intrinsic_depth
                }
            ext_param_x, ext_params_y, ext_param_z = coordinateConverter.intrinsicParamConvert(params)
        elif x in x_third and y in y_third:
            print('I am running within the third elif statement ')
            intrinsic_depth = 91 # This is in inches
            params = {
                'intr_x': x,
                'intr_y': y,
                'depth': intrinsic_depth
            }
            ext_param_x, ext_params_y, ext_param_z = coordinateConverter.intrinsicParamConvert(params)
        elif x in x_four and y in y_four:
            print('I am running within the final elif statement ')
            intrinsic_depth = 141 # This is in inches
            params = {
                'intr_x': x,
                'intr_y': y,
                'depth': intrinsic_depth
            }
            ext_param_x, ext_params_y, ext_param_z = coordinateConverter.intrinsicParamConvert(params)               

        # Left Front Corner Depth
        # for x in np.arange(0.75, 0.80) and y in np.arange(0.79, 0.85):
        #     intrinsic_depth = 96 # This is in inches
        #     params = {
        #         'intr_x': x,
        #         'intr_y': y,
        #         'depth': intrinsic_depth
        #     }
        #     ext_param_x, ext_params_y, ext_param_z = coordinateConverter.intrinsicParamConvert(params)
        # # Left Back Corner Depth
        # for x in np.arange(0.86, 0.91) and y in np.arange(0.82, 0.87):
        #     intrinsic_depth = 141 # This is in inches
        #     params = {
        #         'intr_x': x,
        #         'intr_y': y,
        #         'depth': intrinsic_depth
        #     }
        #     ext_param_x, ext_params_y, ext_param_z = coordinateConverter.intrinsicParamConvert(params)
        # # Right Front Corner
        # for x in np.arange(0.85, 0.90) and y in np.arange(0.80, 0.85):
        #     intrinsic_depth = 91 # This is in inches
        #     params = {
        #         'intr_x': x,
        #         'intr_y': y,
        #         'depth': intrinsic_depth
        #     }
        #     ext_param_x, ext_params_y, ext_param_z = coordinateConverter.intrinsicParamConvert(params)
        # # Right Back Corner
        # for x in np.arange(0.89, 0.94) and y in np.arange(0.80, 0.85):
        #     intrinsic_depth = 141 # This is in inches
        #     params = {
        #         'intr_x': x,
        #         'intr_y': y,
        #         'depth': intrinsic_depth
        #     }
        #     ext_param_x, ext_params_y, ext_param_z = coordinateConverter.intrinsicParamConvert(params)
        # Fraem Center Point (This will be updated to include the dead center depth information)

        print('Converted coordinates to their world coordinates')

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()