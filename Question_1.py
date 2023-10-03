# Imports
import numpy as np

# Simplify the print outputs
np.set_printoptions(suppress=True)

# Define the angles in degrees and convert them to radians
theta_1 = 90*np.pi/180
theta_2 = 180*np.pi/180

# Obtain the skew-symmetric matrices for each of the axes around which rotations happen
x_hat_bracket = np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
z_hat_bracket = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]])

# Calculate the rotation matrices using Rodrigue's formula
e_x_hat_bracket_theta_1 = np.identity(3) + np.sin(theta_1)*x_hat_bracket + (1 - np.cos(theta_1))*np.matmul(x_hat_bracket, x_hat_bracket)
e_z_hat_bracket_theta_2 = np.identity(3) + np.sin(theta_2)*z_hat_bracket + (1 - np.cos(theta_2))*np.matmul(z_hat_bracket, z_hat_bracket)

# Print the matrices so far
print("\ne_x_hat_bracket = ")
print(e_x_hat_bracket_theta_1)
print("\ne_z_hat_bracket = ")
print(e_z_hat_bracket_theta_2)

# Calculate the final rotation matrix product of exponentials 
R = np.matmul(e_x_hat_bracket_theta_1, e_z_hat_bracket_theta_2)

# Print the final rotation matrix
print("\nFinal rotation matrix is = ")
print(R)