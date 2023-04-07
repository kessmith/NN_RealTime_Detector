import numpy as np

# Declare camera calibration matrix
# pixel_coord == (x,y,-d) --> (20, 40, -100)
pixel_coord = np.array([20, 40, -100])
cam_matrix = np.array([[427.340680, 0, 319.454590], [0, 426.1759614, 228.986480], [0, 0, 1]])
# proj_matrix = np.array([[440.231506, 0, 218.503853, 0], [0, 438.913300, 228.332489, 0], [0, 0, 1, 0]])
print(cam_matrix)

print('---------------------------------------------------------------------------')

inv_cam_matrix = np.linalg.inv(cam_matrix)
# Taking inverse of cam_matrix will make the equation as follows:
# X = (inverse P)*x
# X: 3D world coordinate
# P = Project Matrix
# x = 2D pixel coordinate

# The proj_matrix always throwing an error whenever I attemtpt to run the inverse logic on it. So we are going to prove out all the rules associated with taking the inverse of any value.
# det = np.linalg.det(cam_matrix)
world_coord = pixel_coord.dot(inv_cam_matrix)
print(world_coord)