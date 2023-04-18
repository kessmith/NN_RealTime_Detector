#!/usr/bin/env python
import cv2
import numpy as np

class slamLogicHandler:
    def __init__(self):
        pass
    
    def intrinsicParamConvert(self, params):
        # Params De-construction
        pixel_coord = np.array([params['intr_x'], params['intr_y'], params['depth']])
        # focal_length = params['foc_length']
        print('2D Position: ', pixel_coord)
        camera_matrix = np.array([[427.340680, 0, 319.454590], [0, 426.1759614, 228.986480], [0, 0, 1]])
        inv_cam_matrix = np.linalg.inv(camera_matrix)

        world_coord = pixel_coord.dot(inv_cam_matrix)
        print('3D Coordinates: ', world_coord)
        return world_coord[0], world_coord[1], world_coord[2]