# Imports
import numpy as np

# The user defines their 3X3 matrix here!
matrix = np.array([[-1/np.sqrt(2), 1/np.sqrt(2), 0], [-1/2, -1/2, 1/np.sqrt(2)], [1/2, 1/2, 1/np.sqrt(2)]])

# Define the tolerance for the check
tolerance = 1e-5

# The two conditions for a rotation matrix are:
# 1. The determinant of the matrix must be 1 or -1 (with a tolerance in this case). This is the orientation-preserving constraint!
# 2. Its transpose must be equal to its inverse (with the given tolerance in this case). This is the orthogonality constraint!
# Obtain the determinant, inverse, and tranpose of the matrix. 
det = np.linalg.det(matrix)
inv = np.linalg.inv(matrix)
transpose = matrix.T

# Show the input matrix to the user
print(f"\nThe given matrix is =\n{matrix}")
print(f"\nThe determinant of this matrix is =\n{det}")
print(f"\nThe inverse of this matrix =\n{inv}")
print(f"\nThe transpose of this matrix =\n{transpose}")


# IF the two conditions are met, then it IS a rotation matrix!
if (((det >= 1-tolerance and det <= 1 + tolerance) or (det >= -1-tolerance and det <= -1 + tolerance)) and
    (np.allclose(inv, transpose, tolerance))): 
    print("\nThis IS a rotation matrix!\n")

# If they are not met, let the user know AND tell them specifically which constraint(s) was not met!
else:
    print("\nThis is NOT a rotation matrix!")
    if not ((det >= 1-tolerance and det <= 1 + tolerance) or (det >= -1-tolerance and det <= -1 + tolerance)):
        print("The orientation-preserving constraint was not met!")
    if not (np.allclose(inv, transpose, tolerance)):
        print("The orthogonality constraint was not met!")