import numpy as np

# Given the rotation matrix
R_desired = np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])

# We obtain the r's
r11 = R_desired[0][0]
r12 = R_desired[0][1]
r13 = R_desired[0][2]
r21 = R_desired[1][0]
r22 = R_desired[1][1]
r23 = R_desired[1][2]
r31 = R_desired[2][0]
r32 = R_desired[2][1]
r33 = R_desired[2][2]

# We obtain theta by:
theta_rad = np.arccos((r11 + r22 + r33 -1)/2)
theta_deg = theta_rad*180/np.pi

print(f"Theta = {theta_rad} rads\nTheta = {theta_deg} deg.")

# Now obtain w
if np.sin(theta_rad) != 0:
    w_bracket = (1/(2*np.sin(theta_rad)))*(R_desired - R_desired.T)
    print(f"w_bracket =\n{w_bracket}")
else:
    print("\nsin(theta) is undefined! You would need to write the code to deal with this situation!")