#!/usr/bin/env python
import cv2
import numpy as np
import pandas as pd

class SlamLogicHandler:
    def __init__(self, num_cameras):
        self.num_cameras = num_cameras
        self.camera_matrices = []

    def addCameraMatrix(self, camera_matrix):
        # Add camera matrix to the list
        self.camera_matrices.append(camera_matrix)

    def intrinsicParamConvert(self, pixel_coords_list):
        if len(pixel_coords_list) != self.num_cameras:
            raise ValueError("Number of pixel coordinate lists does not match the number of cameras.")

        world_coords_list = []
        
        for i in range(self.num_cameras):
            pixel_coord = np.array(pixel_coords_list[i])
            
            print(f'Camera {i + 1} - 2D Position: ', pixel_coord)

            # Use the corresponding camera matrix for each camera
            camera_matrix = np.array(self.camera_matrices[i])

            # Computes the inverse of a camera matrix --> Results in the identity matrix of the original (camera_matrix) matrix
            inv_cam_matrix = np.linalg.inv(camera_matrix)

            # Calculates the dot product using the inverse camera matrix and the pixel coordinates provided --> Produces the world (3D) coordinates of the originally detected image/frame
            world_coord = pixel_coord.dot(inv_cam_matrix)
            print(f'Camera {i + 1} - 3D Coordinates: ', world_coord)

            world_coords_list.append(world_coord)

        # Returning the world coordinates back for the user to view
        return world_coords_list